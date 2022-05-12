from statistics import mode
import fasttext
from nltk import word_tokenize
from nltk.corpus import stopwords
import re

stop_words = set(stopwords.words('english'))
english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
stop_words.update(english_punctuations)

special_words = {'3d':['3d'],'iot':['iot'],'elearning':['elearning'],'it':['it'],'ecommerce':['ecommerce']}

need_replace_words = {'Text/Captioning':'Captioning','Edit/Processing-Text':'Processing-Text',\
                    'Edit/Processing-Image':'Processing-Image','Names Entity Recognition - NER':'Names Entity Recognition',\
                    'Amazon SageMaker Ground Truth Services':'Ground Truth','Edit/Processing-Video':'Processing-Video',\
                    'Text/OCR':'OCR','ELT/ETL':'Extract-Transform-Load','Continuous Integration and Continuous Delivery':'Continuous Integration Delivery'}

model = None
def load_model():
    global model

    model = fasttext.FastText.load_model('./trained_models/fasttext_model_service.bin')

def _replacer(text):
    replacement_patterns = [
        (r'won\'t', 'will not'),
        (r'can\'t', 'cannot'),
        (r'i\'m', 'i am'),
        (r'ain\'t', 'is not'),
        (r'(\w+)\'ll', r'\g<1> will'),
        (r'(\w+)n\'t', r'\g<1> not'),
        (r'(\w+)\'ve', r'\g<1> have'),
        (r'(\w+)\'s', r'\g<1> is'),
        (r'(\w+)\'re', r'\g<1> are'),
        (r'(\w+)\'d', r'\g<1> would')]
    patterns = [(re.compile(regex), repl) for (regex, repl) in replacement_patterns]
    s = text
    for (pattern, repl) in patterns:
        (s, _) = re.subn(pattern, repl, s)
    return s

        
def my_tokenize(seq):
    seq = re.sub('https?://\S* ', '', seq)
    seq = _replacer(seq)  
    for k,v in need_replace_words.items():
        seq = seq.replace(k,v)
    a = word_tokenize(seq)
    b = []
    for word in a:
        if word.lower() in special_words:
            b.extend(special_words[word.lower()])
        else:
            candidates = list(filter(lambda x : x.strip() != '',word.split('-')))
            for candidate in candidates:
                pre = ''
                for chr in candidate:
                    if not chr.isalpha():
                        if pre != '':
                            b.append(pre.lower())
                            pre = ''
                    else:
                        if chr.islower():
                            pre += chr
                        else:
                            if pre == '':
                                pre += chr
                            else:
                                if pre[-1].islower():
                                    b.append(pre.lower())
                                    pre = chr
                                else:
                                    pre += chr
                if pre != '':
                    b.append(pre.lower())
    b = [x for x in b if x not in stop_words and not x.isdigit()]
    return b

def predict(des, k=5):

    if model is None:
        load_model()
    res = model.predict(' '.join(my_tokenize(des)), k=k)
    d = {}
    for name,prob in zip(*res):
        d[name.replace('__label__', '')] = max(round(prob, 2), 0.01)
    return d


if __name__ == '__main__':
    des = 'The 99 Corp service enables the use of API endpoints for enterprise 99 clients that includes; Companies, Contributors, Cost Centers and more. Requests use an access token for the authentication process, with the named API Key to be included with the access token value in the HTTP header. 99 Corp provides a taxi management platform that allows you to register your company and employees and track the races of your business in real time, make centralized payments with no reimbursement and complexity, customize reports, cost center and more.'
    print(predict(des))
    # model = fasttext.train_supervised(input="../file/fasttext_train.txt",  lr=0.5, epoch=25, wordNgrams=2, bucket=200000, dim=50, loss='ova')