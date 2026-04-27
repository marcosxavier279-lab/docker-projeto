import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_content(self):
        response = self.app.get('/')
        self.assertEqual(response.data.decode('utf-8'), "Hello, Docker!")

    def test_home_not_empty(self):
        response = self.app.get('/')
        self.assertTrue(len(response.data) > 0)

    def test_home_type(self):
        response = self.app.get('/')
        self.assertIsInstance(response.data.decode('utf-8'), str)

    def test_home_contains_word(self):
        response = self.app.get('/')
        self.assertIn("Docker", response.data.decode('utf-8'))

if __name__ == "__main__":
    unittest.main()
