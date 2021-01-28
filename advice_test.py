import unittest
import advice as tested_app
import json




class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()

    def test_good_advice(self):
        r = self.app.get('/goodadvice')
        
        self.assertIn(r.data.decode('ascii'),tested_app.good_advice_list )

    def test_bad_advice(self):
        r = self.app.get('/badadvice')
        self.assertIn(r.data.decode('ascii'), tested_app.bad_advice_list)



if __name__ == '__main__':
    unittest.main()