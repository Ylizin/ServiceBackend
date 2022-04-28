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
    return {'status':r,'class_res':'test'}

@app.post("/match",response_model=MatchResponseModel)
def match(info : RequestInfo):
    r = ResponseStatus()
    r.status = 400
    r.message = 'success'
    logger.debug(info)
    return {'status':r,'match_res':[]}
