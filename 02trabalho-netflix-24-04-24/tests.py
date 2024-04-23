import pytest
from init import app, db


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()


def test_register_new_user(client):
    response = client.post('/api/register',
                           json={'username': 'testuser', 'email': 'testuser@test.com', 'password': 'testpassword'})
    assert response.status_code == 201
    assert b'User registered successfully.' in response.data


def test_register_existing_user(client):
    client.post('/api/register',
                json={'username': 'testuser', 'email': 'testuser@test.com', 'password': 'testpassword'})
    response = client.post('/api/register',
                           json={'username': 'testuser', 'email': 'testuser@test.com', 'password': 'testpassword'})
    assert response.status_code == 400
    assert b'User already exists.' in response.data


def test_login_valid_user(client):
    client.post('/api/register',
                json={'username': 'testuser', 'email': 'testuser@test.com', 'password': 'testpassword'})
    response = client.post('/api/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert b'User logged in successfully.' in response.data


def test_login_invalid_user(client):
    response = client.post('/api/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 401
    assert b'Invalid username or password.' in response.data


def test_content(client):
    response = client.get('/api/content')
    assert response.status_code == 200


def test_content_detail_valid_content(client):
    response = client.get('/api/content/1')
    assert response.status_code == 200


def test_content_detail_invalid_content(client):
    response = client.get('/api/content/100')
    assert response.status_code == 404
    assert b'Content not found.' in response.data


def test_play_valid_content(client):
    client.post('/api/register',
                json={'username': 'testuser', 'email': 'testuser@test.com', 'password': 'testpassword'})
    response = client.get('/api/play/1/1')
    assert response.status_code == 200
    assert b'Playing content:' in response.data


def test_play_invalid_content(client):
    client.post('/api/register',
                json={'username': 'testuser', 'email': 'testuser@test.com', 'password': 'testpassword'})
    response = client.get('/api/play/100/1')
    assert response.status_code == 404
    assert b'Content not found.' in response.data


def test_history_valid_user(client):
    client.post('/api/register',
                json={'username': 'testuser', 'email': 'testuser@test.com', 'password': 'testpassword'})
    client.get('/api/play/1/1')
    response = client.get('/api/history/1')
    assert response.status_code == 200


def test_search(client):
    response = client.get('/api/search?title=The Shawshank Redemption')
    assert response.status_code == 200


def test_create_playlist(client):
    client.post('/api/register',
                json={'username': 'testuser', 'email': 'testuser@test.com', 'password': 'testpassword'})
    response = client.post('/api/playlist', json={'user_id': 1, 'content_id': 1})
    assert response.status_code == 201
    assert b'Playlist created successfully.' in response.data
