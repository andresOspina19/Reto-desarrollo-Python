from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

#Least Common Multiple (LCM)
def test_get_LCM_from_numbers():
    response = client.get('/math/lcm/', data={ 'numbers': [4, 8, 15, 25] })
    assert response.status_code == 200
    assert response.json() == {'LCM': 600}
    
    response = client.get('/math/lcm/', data={ 'numbers': [9, 8] })
    assert response.status_code == 200
    assert response.json() == {'LCM': 72}
    
    response = client.get('/math/lcm/', data={ 'numbers': ["hola"] })
    assert response.status_code == 422
    

def test_get_number_plus_one():
    response = client.get("/math/", data={ 'number':  2})
    assert response.status_code == 200
    assert response.json() == {'numberPlusOne': 3}
    
    response = client.get("/math/", data={ 'number':  512.5})
    assert response.status_code == 200
    assert response.json() == {'numberPlusOne': 513.5}
    
    response = client.get("/math/", data={ 'number':  "hola"})
    assert response.status_code == 422
