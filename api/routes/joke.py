from fastapi import APIRouter
from typing import Optional
from models.joke import getJokeOptions
from config.db import connection
from bson import ObjectId

router = APIRouter()

@router.get('/jokes/', tags=["Jokes Methods"])
def get_random_joke_from_local_database():
    pass

@router.get('/jokes/{value}', tags=["Jokes Methods"])
def get_joke(value: getJokeOptions):
    pass

@router.post('/jokes/', tags=["Jokes Methods"])
def save_joke():
    pass

@router.put('/jokes/{}', tags=["Jokes Methods"])
def update_joke():
    pass

@router.delete('/jokes/', tags=["Jokes Methods"])
def delete_joke():
    pass