from os import stat
from re import S

from yaml import load
from model import ClassifyResponseModel, RequestInfo, ResponseStatus, MatchResponseModel,AllServiceResponseModel,ServiceInfo
from read_test_data import test_match,pw_df
from fastapi import FastAPI,Path
from fastapi.middleware.cors import CORSMiddleware
from cls.inference import load_model, predict
from match.match import match_text
import logging
logger = logging.getLogger("gunicorn.error")

app = FastAPI()

origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event('startup')
def start():
    load_model()


@app.post("/classify", response_model=ClassifyResponseModel)
def classify(info: RequestInfo):
    r = ResponseStatus()
    r.status = 400
    r.message = 'success'
    logger.debug(info)
    class_res = [{'service_class':k,'possibility':v} for k,v in predict(info.req_text).items()]
    return {'status': r, 'class_res': class_res}


@app.post("/match", response_model=MatchResponseModel)
def match(info: RequestInfo):
    r = ResponseStatus()
    r.status = 400
    r.message = 'success'
    logger.debug(info)
    res = match_text(info.req_text)
    match_res = pw_df.iloc[res]
    
    # match_res = [
    #     {
    #         'service_name' : 'test_service',
    #         'service_description' : 'blabla',
    #         'service_tags' : ['tag1','tag2','tag3'],
    #         'match_score' : 0.8
    #     }
    # ]
    return {'status': r, 'match_res': __pack_df_data(match_res)}


@app.get(r'/all/{page_id}/{page_num}',response_model=AllServiceResponseModel)
def getall_sevrice(page_id: int = Path(...,title = "page id",ge=1),page_num : int = Path(...,ge = 3,le = 50)):
    """
    all_sercice return page info and totle len, from (page_id-1)*pageNum to page_id*pageNum -1 both included. 
                page_id > 1
                page_num >3 
    Args:
        page_id (int, optional): _description_. Defaults to Path(...,title = "page id",ge=1).
        page_num (int, optional): _description_. Defaults to Path(...,ge = 3).
    """
    all_len = len(pw_df)
    start = (page_id-1)*page_num
    end = page_id*page_num 
    logger.debug('{},{}'.format(page_id,page_num))
    all_service = []
    r = ResponseStatus()
    if start>=all_len :
        r.status = 300
        r.message = 'page exceed'
    else:
        data = pw_df.iloc[start:end]
        all_service += __pack_df_data(data)
        r.status = 400
        r.message = 'success'
    return {'status':r, 'all_count':all_len,'all_service':all_service}


def __pack_df_data(df):
    service_li = []
    for tup in df.itertuples():
        build_dict = {
            'service_name':tup.Name,
            'service_description':tup.Description,
            'service_tags':eval(tup.Categories)
            }
        service_li.append(ServiceInfo(**build_dict))
    return service_li