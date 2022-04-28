from pydantic import BaseModel
from typing import List, Optional

from soupsieve import match


class ResponseStatus(BaseModel):
    status : int  = 0
    message: str  = 'req received'


class RequestInfo(BaseModel):
    id_token: Optional[str] = None
    req_type: int = -1
    req_text: str = ''


class ClassifyResponseModel(BaseModel):
    status: ResponseStatus
    class_res: str


class MatchService(BaseModel):
    service_name: str
    service_description: str
    service_tags: List[str]
    match_score: float

class MatchResponseModel(BaseModel):
    status: ResponseStatus
    match_res: List[MatchService] = []