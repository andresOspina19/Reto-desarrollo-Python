from fastapi.testclient import TestClient
from app import app
from config.db import connection
from bson import ObjectId
import requests
import json

client = TestClient(app)

def test_get_random_joke_from_local_database():
    response = client.get('/jokes/')
    assert response.status_code == 200
    assert response.json()["source"] == "local"
    
    #Checking if it really exists in the database
    joke = connection.local.joke.find_one({"_id": ObjectId(response.json()["number"])})
    assert response.json()['text'] == joke['text']


def test_get_joke_with_chuck():
    response = client.get('/jokes/Chuck')
    assert response.status_code == 200
    assert response.json()["source"] == "https://api.chucknorris.io/"
    text = response.json()["text"] 
    
    #Checking if it really exists in the chucknorris API
    response_chuck = requests.get(f"https://api.chucknorris.io/jokes/search?query={text}")
    assert response_chuck.status_code == 200
    assert response_chuck.json()['total'] >= 1


def test_get_joke_with_dad():
    response = client.get('/jokes/Dad')
    assert response.status_code == 200
    assert response.json()["source"] == "https://icanhazdadjoke.com/api"
    id = response.json()["number"] 
    
    #Checking if it really exists in the chucknorris API
    response_dad = requests.get(f"https://icanhazdadjoke.com/j/{id}",
                                  headers={'Accept': 'application/json'})
    assert response_dad.status_code == 200
    assert response_dad.json()['id'] == id


def test_save_update_delete_joke():
    data = {
        "text": "This is a joke for the sake of testing the API",
    }
    response = client.post('/jokes/', json=json.dumps({data}))
    
    #Checking if it was saved successfully
    assert response.status_code == 200
    assert response.json()['text'] == data['text']
    assert response.json()['source'] == 'local' 
    
    
    update_data = {
        "number": response.json()['number'],
        "text": "This joke is being updated to test the update method :)"
    }
    update_response = client.put('/jokes/', json=json.dumps({update_data}))
    
    #Checking if it was updated successfully
    assert update_response.status_code == 200
    assert update_response.json()['text'] == update_data['text']
    assert update_response.json()['source'] == 'local' 
    
    
    delete_data = {
        "number": response.json()['number']
    }
    delete_response = client.delete('/jokes/', json=json.dumps({delete_data}))
   
    #Checking if it was deleted successfully
    assert update_response.status_code == 200
    assert connection.local.joke.find_one({'_id': ObjectId(delete_data['number'])}) == None
    