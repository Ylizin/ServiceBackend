#%%
import torch
import pickle 
from torch import nn

param = torch.load('./trained_models/encoder_param')
all_f = pickle.load(open('./trained_models/all_feature.tsr','rb'))
di = pickle.load(open('./trained_models/dict','rb'))

encoder = nn.Embedding(20000,500)
encoder.load_state_dict(param)
# %%

cos = nn.CosineSimilarity()
from .eda import lem
#%%
def match_text(text):
    text1 = torch.tensor([di.token2id[w] for w in filter(lambda x: x in di.token2id,lem(text))]).to(torch.long)
    vec = torch.mean(encoder(text1),dim = 0,keepdim=True)
    sims = cos(vec,all_f)
    sims_sort = sims.argsort(dim = -1,descending=True)
    res = sims_sort[:20].tolist()
    return res, sims[res].tolist()
# # %%
# text = 'government data data nordic'

# print(match_text(text))

# %%
