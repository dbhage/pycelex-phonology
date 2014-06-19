'''
Created on Jun 11, 2014

@author: dbhage

Test Suite to run all of the tests in one go.

'''

import unittest
from test.phonology.english_celex_test import EnglishCelexTest
from test.factory.factory_test import CelexFactoryTest

def suite():
    suite = unittest.TestSuite()
    suite.addTests([CelexFactoryTest(), 
                    EnglishCelexTest()])
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)