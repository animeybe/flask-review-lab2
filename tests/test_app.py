from app import app


def test_index():
    response = app.test_client().get("/")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Hello, World!"


def test_missing_page():
    response = app.test_client().get("/missing")
    assert response.status_code == 404

def test_about():
    response = app.test_client().get("/about")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "About this laboratory project"

def test_health():
    response = app.test_client().get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}

def test_version():
    response = app.test_client().get("/version")
    assert response.status_code == 200
    assert response.get_json() == {"version": "0.1.0"}