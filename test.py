import os
import unittest
import json
from database.models import get_word_data
from flaskr import *


class ComplimentTestCase(unittest.TestCase):

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.word_data = get_word_data()
    
    def tearDown(self):
        """Executed after reach test"""
        pass
    #=======helper functions===========
    def parse_compliment(self, compliment):
        opening = compliment[:10]
        closing = compliment[10:]
        noun = closing.split(' ')[-1]
        adjectives = [adjective.replace(',','') for adjective in closing.split(' ')[:-1]]
        return opening, adjectives, noun

    #======= tests ==========
    def test_get_compliment(self):
        number_of_adjectives=700
        res = self.client().get('/compliment/'+str(number_of_adjectives))
        data = json.loads(res.data)
        opening, adjectives, noun = self.parse_compliment(data['compliment'])
        
        self.assertTrue(set(adjectives).issubset(set(self.word_data['positive_adjectives'])))
        self.assertEqual(len(adjectives),number_of_adjectives)
        self.assertTrue(noun in self.word_data['positive_nouns'] )

if __name__ == "__main__":
    unittest.main()