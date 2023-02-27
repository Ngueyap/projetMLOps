import unittest
import pandas as pd
from vector import text_to_vector
import pickle


class MyTest(unittest.TestCase):    

    df = pd.read_csv('test.csv')

    def test_text_to_vector(self):
        result = text_to_vector('je suis un eleve dans une classe d assassins notre objectif est de tuer notre professeur')
        self.assertEqual(result, 0.00014480953)

    def test_predict(self):
        df = df.drop(['Rating', 'Unnamed: 0'], axis=1)
        with open('model.pkl', 'rb') as f:
            model = pickle.load(f)
        result = model.predict(df)
        self.assertEqual(result, 5.532)
