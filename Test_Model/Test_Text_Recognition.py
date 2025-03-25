import sys
import unittest
import pandas as pd
from pandas import DataFrame
from difflib import SequenceMatcher
import warnings

from pandas.errors import ParserWarning

engine = 'python'


class MyTestCase(unittest.TestCase):
    @staticmethod
    def test_data_init():
        tester: DataFrame
        tested: DataFrame
        test_dict: dict

        TEST_DIR = 'test/'
        tester_file_name = 'testthetest.csv'
        tested_file_name = 'tobetested.csv'
        try:
            tester = pd.read_csv(TEST_DIR + tester_file_name, sep = ', ', header = 0)
            tested = pd.read_csv(TEST_DIR + tested_file_name, sep = ', ', header = 0)


        except IOError:
            print('Unable to locate test file(s)')
            sys.exit()
        test_dict = {'tester': tester, 'tested': tested}
        return test_dict


    def test_accuracy(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        warnings.filterwarnings("ignore", category=ParserWarning)
        accuracy: float
        sum_accuracy: float
        tester: DataFrame
        tested: DataFrame

        test_dict = self.test_data_init()
        tester = test_dict['tester']
        tested = test_dict['tested']
        sum_accuracy = 0.0

        if tester.size != tested.size:
            print('incomparable test data!')
            sys.exit()

        combined_test = tester.join(tested)

        for index, row in combined_test.iterrows():
            expected_value = row['input']
            output_value = row['output']

            sum_accuracy += SequenceMatcher(None, expected_value, output_value).ratio()

        try:
            accuracy = sum_accuracy/len(tester['input'])
            self.assertTrue(accuracy >= 0.7)
            print('Model accuracy test passed with an accuracy of', (int)(round(accuracy, 2) * 100), '%')

        except ZeroDivisionError:
            print('empty tester!')



if __name__ == '__main__':
    unittest.main()
