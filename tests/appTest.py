import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_print_health_check(self):
        response = self.app.get('/health-check')
        self.assertEqual(200, response.status_code, "Erro no test_http_code!")
        self.assertEqual("<h1>Hello, I'm Alive!</h1>", response.get_data(as_text=True)
                          , "Erro no test_print_health_check!")

    def test_print_hello_sucess(self):

        response = self.app.get('/hello?name=Daniel')
        self.assertEqual(200, response.status_code)
        self.assertEqual("Hello, Daniel!", response.get_data(as_text=True))

    def test_print_hello_error(self):

        response = self.app.get('/hello')
        self.assertEqual(400, response.status_code)