from typing import Optional
from pydantic import BaseModel

class Joke(BaseModel):
    number: Optional[str]
    text: str