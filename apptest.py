import unittest
import advice as tested_app
import json

good_advice_list = tested_app.good_advice_list

bad_advice_list = tested_app.bad_advice_list


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        tested_app.app.config['TESTING'] = True
        self.app = tested_app.app.test_client()


    def test_good_advice(self):
        r = self.app.get('/goodadvice')
        
        self.assertIn(r.data,good_advice_list )

    def test_bad_advice(self):
        r = self.app.get('/badadvice')
        self.assertEqual(r.data, bad_advice_list)