from app import app


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, World!"


def test_missing_page():
    response = app.test_client().get("/missing")
    assert response.status_code == 404