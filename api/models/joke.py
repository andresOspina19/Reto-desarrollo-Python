from typing import Optional
from pydantic import BaseModel
from enum import Enum

class Joke(BaseModel):
    number: Optional[str]
    text: str

class getJokeOptions(str, Enum):
    chuck = "Chuck"
    dad = "Dad"