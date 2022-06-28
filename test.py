import unittest
import main

text = "Today is the hottest day on planet earth"

class TestNgram(unittest.TestCase):

    def test_unigram(self):
        result_1gram = [['Today'], ['hottest'], ['day'], ['planet'], ['earth']]
        self.assertListEqual(main.generate_N_gram(text=text, n_gram = 1), result_1gram)

    def test_bigram(self):
        result_2gram = [['Today', 'hottest'], ['hottest', 'day'], ['day', 'planet'], ['planet', 'earth']]
        self.assertListEqual(main.generate_N_gram(text=text, n_gram=2), result_2gram, msg="ListNotEqual")
    
    def test_trigram(self):
        result_3gram = [['Today', 'hottest', 'day'], ['hottest', 'day', 'planet'], ['day', 'planet', 'earth']]
        self.assertListEqual(main.generate_N_gram(text=text, n_gram=3), result_3gram)
        


if __name__ == "main":
    unittest.main()