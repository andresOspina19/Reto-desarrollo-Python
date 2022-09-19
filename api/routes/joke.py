from fastapi import APIRouter, HTTPException, Response
from typing import Optional
from models.joke import getJokeOptions, JokeNumber, Joke, JokeNumberMandatory
from schemas.joke import localJokeEntity, chuckNorrisJokeEntity, dadJokeEntity
from config.db import connection
from bson import ObjectId
import requests
from starlette.status import HTTP_204_NO_CONTENT

router = APIRouter()

@router.get('/jokes/', tags=["Jokes Methods"])
def get_random_joke_from_local_database():
    #getting a random joke from the collection 'joke' of the database
    random_joke = list(connection.local.joke.aggregate([{ '$sample': { 'size': 1 } }]))[0]
    return localJokeEntity(random_joke)

@router.get('/jokes/{value}', tags=["Jokes Methods"])
def get_joke(value: getJokeOptions):
    if value.value == "Chuck":
        chuck_joke = requests.get("https://api.chucknorris.io/jokes/random").json()
        return chuckNorrisJokeEntity(chuck_joke)
    elif value.value == "Dad":
        dad_joke = requests.get("https://icanhazdadjoke.com/", headers={'Accept': 'application/json'}).json()
        return dadJokeEntity(dad_joke)
    else:
        raise HTTPException(status_code=422, detail="Please select between Chuck and Dad")
        

@router.post('/jokes/', tags=["Jokes Methods"])
def save_joke(joke: Joke):
    number = connection.local.joke.insert_one(dict(joke)).inserted_id
    joke = connection.local.joke.find_one({'_id': number})
    return localJokeEntity(joke)

@router.put('/jokes/', tags=["Jokes Methods"])
def update_joke(joke: JokeNumberMandatory):
    joke = dict(joke)
    connection.local.joke.find_one_and_update({'_id': ObjectId(joke['number'])}, {'$set':joke})
    updated_joke = connection.local.joke.find_one({'_id': ObjectId(joke['number'])})
    return localJokeEntity(updated_joke)
    

@router.delete('/jokes/', tags=["Jokes Methods"])
def delete_joke(jokeNumber: JokeNumber):
    number = dict(jokeNumber)["number"]
    connection.local.joke.find_one_and_delete({'_id': ObjectId(number)})
    return Response(status_code=HTTP_204_NO_CONTENT)