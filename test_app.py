from unittest import TestCase
from app import app
from flask import session,jsonify   
from boggle import Boggle


class FlaskTests(TestCase):

    # TODO -- write tests for every view function / feature!

    def test_home(self):
        with app.test_client() as client:
            response = client.get('/')

            self.assertEqual(response.status_code, 200)
            self.assertIn('board', session)
            self.assertIsNone(session.get('highscore'))
            self.assertIsNone(session.get('attempt'))
            self.assertIn('board', session)
    
    def test_submit(self):
        with app.test_client() as client:
             with client.session_transaction() as sesh:
                 sesh['board']=[
                    ["T", "E", "S", "T"],
                    ["T", "E", "S", "T"],
                    ["T", "E", "S", "T"],
                    ["T", "E", "S", "T"],
                    ]
                    
        response = client.post('/submit/test')
        self.assertEqual(response.json['word'], 'test')
        self.assertEqual(response.json['result'], 'ok')


    def test_score(self):
        with app.test_client() as client:
             with client.session_transaction() as sesh:
                # add items to session in flask
                sesh['attempt']=3
                sesh['highscore']= 4

        response = client.post('/score')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['record'], 0)


