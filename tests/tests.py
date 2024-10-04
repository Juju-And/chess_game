from src.app import app
from src.chess import King, Queen
import pytest


def test_king_available_moves():
    king = King("f5")
    assert sorted(king.list_available_moves) == sorted(
        ["e5", "g5", "f6", "f4", "e6", "e4", "g6", "g4"]
    )


def test_king_valid_moves():
    king = King("f5")
    assert king.validate_move("e5") == "valid"
    assert king.validate_move("e8") == "not valid"


def test_queen_available_moves():
    queen = Queen("d4")
    assert sorted(queen.list_available_moves) == sorted(
        ["c4", "e4", "d5", "d3", "c5", "c3", "e5", "e3"]
    )


def test_queen_valid_moves():
    queen = Queen("d4")
    assert queen.validate_move("e4") == "valid"
    assert queen.validate_move("e8") == "not valid"


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_valid_figure_response_code(client):
    response = client.get("/api/v1/knight/h1")
    assert response.status_code == 200


def test_invalid_figure_response_code(client):
    response = client.get("/api/v1/dummy/h1")
    assert response.status_code == 404


def test_invalid_field_response_code(client):
    response = client.get("/api/v1/king/h15")
    assert response.status_code == 409
