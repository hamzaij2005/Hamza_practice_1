import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_health(client):
    res = client.get('/api/health')
    assert res.status_code == 200

def test_get_students(client):
    res = client.get('/api/students')
    assert res.status_code == 200
    assert isinstance(res.get_json(), list)

def test_get_nonexistent_student(client):
    res = client.get('/api/students/999')
    assert res.status_code == 404

def test_add_student_valid(client):
    res = client.post('/api/students', json={"name": "Hamza"})
    assert res.status_code == 201
    assert res.get_json()["name"] == "Hamza"

def test_add_student_invalid(client):
    res = client.post('/api/students', json={})
    assert res.status_code == 400