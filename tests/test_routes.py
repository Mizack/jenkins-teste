import pytest

from app.routes import app

@pytest.fixture

def client():
    with app.test_client() as client:
        yield client


def test_home_page_returns_200(client):
    """
    Test if the home page returns a status code of 200.
    """
    response = client.get('/')
    assert response.status_code == 200


def test_home_page_contains_hello_message(client):
    """
    Test if the home page contains the expected 'It`s works' message.
    """
    response = client.get('/')
    assert b"It`s works" in response.data