import flaskr
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        print("Preparing")
        # self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        # flaskr.app.testing = True
        # self.app = flaskr.app.test_client()
        # with flaskr.app.app_context():
        #     flaskr.init_db()

    def tearDown(self):
        print("Finishing")
        # os.close(self.db_fd)
        # os.unlink(flaskr.app.config['DATABASE'])

    def test_something(self):
        print("Testing")
        self.assertEqual(b'A string', b'Another')

if __name__ == '__main__':
    unittest.main()
