from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
import logging 
logger = logging.getLogger("gunicorn.error")


app = FastAPI()




from model import ClassifyResponseModel,RequestInfo,ResponseStatus,MatchResponseModel

@app.post("/classify",response_model=ClassifyResponseModel)
def classify(info : RequestInfo):
    r = ResponseStatus()
    r.status = 400
    r.message = 'success'
    logger.debug(info)
    class_res = [{'service_class':'1111','possibility':0.1}]
    return {'status':r,'class_res':class_res}

@app.post("/match",response_model=MatchResponseModel)
def match(info : RequestInfo):
    r = ResponseStatus()
    r.status = 400
    r.message = 'success'
    logger.debug(info)
    match_res = [
        {
            'service_name' : 'test_service',
            'service_description' : 'blabla',
            'service_tags' : ['tag1','tag2','tag3'],
            'match_score' : 0.8
        }
    ]
    return {'status':r,'match_res':match_res}
