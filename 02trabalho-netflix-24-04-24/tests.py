import unittest
import pytest
from init import app, db, User, Content


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_register_new_user(self):
        response = self.app.post('/api/register', json={
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['message'], 'User registered successfully.')

    def test_register_existing_user(self):
        self.app.post('/api/register', json={
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword'
        })
        response = self.app.post('/api/register', json={
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 400)

    def test_login_valid_user(self):
        self.app.post('/api/register', json={
            'username': 'testuser',
            'email': 'testuser@test.com',
            'password': 'testpassword'
        })
        response = self.app.post('/api/login', json={
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()['message'], 'User logged in successfully.')

    def test_login_invalid_user(self):
        response = self.app.post('/api/login', json={
            'username': 'invaliduser',
            'password': 'invalidpassword'
        })
        self.assertEqual(response.status_code, 401)

    def test_content_detail_valid_id(self):
        with app.app_context():
            content = Content(title='Test Content', synopsis='Test Synopsis')
            db.session.add(content)
            db.session.commit()
            content_id = content.id
        response = self.app.get(f'/api/content/{content_id}')
        self.assertEqual(response.status_code, 200)

    def test_content_detail_invalid_id(self):
        response = self.app.get('/api/content/999')
        self.assertEqual(response.status_code, 404)

    def test_search_content(self):
        content = Content(title='Test Content', synopsis='Test Synopsis', genre='Test Genre')
        with app.app_context():
            db.session.add(content)
            db.session.commit()
        response = self.app.get('/api/search', query_string={'title': 'Test Content'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()[0]['title'], 'Test Content')

    def test_create_playlist(self):
        with app.app_context():
            user = User(username='testuser', email='testuser@test.com', password='testpassword')
            content = Content(title='Test Content', synopsis='Test Synopsis')
            db.session.add(user)
            db.session.add(content)
            db.session.commit()
            user_id = user.id
            content_id = content.id
        response = self.app.post('/api/playlist', json={
            'user_id': user_id,
            'content_id': content_id
        })
        self.assertEqual(response.status_code, 201)
