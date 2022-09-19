from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_get_joke():
    pass

def test_save_joke():
    pass

def test_update_joke():
    pass

def test_delete_joke():
    pass