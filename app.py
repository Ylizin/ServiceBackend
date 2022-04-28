from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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
