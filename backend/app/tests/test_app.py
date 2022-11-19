""" Test suite for app """
import pytest_check as check
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_hello_world():
    """Hello World test suite"""

    hello_world = client.get("/")
    check.equal(hello_world.status_code, 200)
    check.equal(hello_world.json(), {"hello": "world"})
