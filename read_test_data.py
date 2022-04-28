#%%
import pandas as pd

# %%
from model import *

test_match = []
test_match.append({
    'service_name':"Ã–rebro kommun", 
    'service_description':"Ã–rebro kommun (Ã–rebro municipality, Sweden) provides an online portal to government data and information, including waste & recycling, libraries, transit, politics, sports & culture, business, tourism, and more. Much of this information can be mapped and a RESTful API can also retrieve this data in XML and JSON. The site and documentation are in Swedish.", 
    'service_tags':['government', 'data', 'data', 'nordic'],
    'match_score':0.1
})

test_match.append({
    'service_name':"30 Boxes", 
    'service_description':"30 Boxes is a calendaring service that allows you to organize your life, then share it with friends. You can also keep track of friends' calendars. 30 Boxes interfaces with Flickr, Livejournal, Blogger, among others. 30 Boxes also supports SMS and e-mail notifications.", 
    'service_tags':['calendars', 'events'],
    'match_score':0.1
})


test_match.append({
    'service_name':"99 Corp REST API v1.0", 
    'service_description':"The 99 Corp service enables the use of API endpoints for enterprise 99 clients that includes; Companies, Contributors, Cost Centers and more. Requests use an access token for the authentication process, with the named API Key to be included with the access token value in the HTTP header. 99 Corp provides a taxi management platform that allows you to register your company and employees and track the races of your business in real time, make centralized payments with no reimbursement and complexity, customize reports, cost center and more.",
    'service_tags':['transportation', 'platform-as-a-service'],    
    'match_score':0.1213123
})

test_match.append({
    'service_name':"AccountingLive REST API v4", 
    'service_description':"The AccountingLive API integrates accounting features into applications such as invoicing, billing, and templates. It is available in REST architecture with HTTP requests and JSON responses, authenticating via basic HTTP.",
    'service_tags':['accounting', 'accounts', 'business', 'invoicing'],   
    'match_score':0.1111
})

test_match.append({
    'service_name':"Ã–rebro kommun", 
    'service_description':"Ã–rebro kommun (Ã–rebro municipality, Sweden) provides an online portal to government data and information, including waste & recycling, libraries, transit, politics, sports & culture, business, tourism, and more. Much of this information can be mapped and a RESTful API can also retrieve this data in XML and JSON. The site and documentation are in Swedish.", 
    'service_tags':['government', 'data', 'data', 'nordic'],
    'match_score':0.1
})

test_match.append({
    'service_name':"AccountingLive REST API v4", 
    'service_description':"The AccountingLive API integrates accounting features into applications such as invoicing, billing, and templates. It is available in REST architecture with HTTP requests and JSON responses, authenticating via basic HTTP.",
    'service_tags':['accounting', 'accounts', 'business', 'invoicing'],   
    'match_score':0.1111
})

test_match.append({
    'service_name':"Ã–rebro kommun", 
    'service_description':"Ã–rebro kommun (Ã–rebro municipality, Sweden) provides an online portal to government data and information, including waste & recycling, libraries, transit, politics, sports & culture, business, tourism, and more. Much of this information can be mapped and a RESTful API can also retrieve this data in XML and JSON. The site and documentation are in Swedish.", 
    'service_tags':['government', 'data', 'data', 'nordic'],
    'match_score':0.1
})


test_match.append({
    'service_name':"AccountingLive REST API v4", 
    'service_description':"The AccountingLive API integrates accounting features into applications such as invoicing, billing, and templates. It is available in REST architecture with HTTP requests and JSON responses, authenticating via basic HTTP.",
    'service_tags':['accounting', 'accounts', 'business', 'invoicing'],   
    'match_score':0.1111
})

test_match.append({
    'service_name':"30 Boxes", 
    'service_description':"30 Boxes is a calendaring service that allows you to organize your life, then share it with friends. You can also keep track of friends' calendars. 30 Boxes interfaces with Flickr, Livejournal, Blogger, among others. 30 Boxes also supports SMS and e-mail notifications.", 
    'service_tags':['calendars', 'events'],
    'match_score':0.1
})

test_match.append({
    'service_name':"AccountingLive REST API v4", 
    'service_description':"The AccountingLive API integrates accounting features into applications such as invoicing, billing, and templates. It is available in REST architecture with HTTP requests and JSON responses, authenticating via basic HTTP.",
    'service_tags':['accounting', 'accounts', 'business', 'invoicing'],   
    'match_score':0.1111
})
