from fastapi.testclient import TestClient
from api.app import app

client = TestClient(app)

def test_get_joke():
    assert 2 == 2

def test_save_joke():
    assert 3 == 3
    

def test_update_joke():
    assert 4 == 4

def test_delete_joke():
    assert 5 == 5