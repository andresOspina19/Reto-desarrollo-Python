from typing import Optional
from pydantic import BaseModel
from enum import Enum

class JokeNumber(BaseModel):
    number: str

class Joke(BaseModel):
    text: str

class JokeNumberMandatory(BaseModel):
    number: str
    text: str

class getJokeOptions(str, Enum):
    chuck = "Chuck"
    dad = "Dad"