'''

Created on Mar 19, 2014

@author: dbhage

CelexFactory Test Class

'''

import unittest

from celex.factory.factory import build_celex

from test import TEST_CELEX_PATH

from celex.phonology.english_celex import EnglishCelex
from celex.phonology.german_celex import GermanCelex
from celex.phonology.dutch_celex import DutchCelex

class CelexFactoryTest(unittest.TestCase):

    def test_case_1(self):
        '''
        Invalid Case: Celex path does not exist
        '''
        path = "/home/dbhage/does_not_exists"
        lang = 0
        version = 0
        self.assertRaises(ValueError, build_celex, path, lang, version)

    def test_case_2(self):
        '''
        Invalid Case: path exists but is not celex path
        '''
        path = "/home/dbhage/piperlab" # this path needs to exist for test to make sense, otherwise its just case 1 again
        lang = 0
        version = 0
        self.assertRaises(ValueError, build_celex, path, lang, version)

    def test_case_3(self):
        '''
        Invalid Case: Language out of range
        '''
        path = "/home/dbhage/celex2"
        lang = 3
        version = 0
        self.assertRaises(ValueError, build_celex, path, lang, version)

    def test_case_4(self):
        '''
        Invalid Case: Language out of range
        '''
        path = "/home/dbhage/celex2"
        lang = -1
        version = 0
        self.assertRaises(ValueError, build_celex, path, lang, version)

    def test_case_5(self):
        '''
        Invalid Case: Version out of range
        '''
        path = "/home/dbhage/celex2"
        lang = 2
        version = 0
        self.assertRaises(ValueError, build_celex, path, lang, version)

    def test_case_6(self):
        '''
        Invalid Case: Version out of range
        '''
        path = "/home/dbhage/celex2"
        lang = 2
        version = 4
        self.assertRaises(ValueError, build_celex, path, lang, version)

    def test_case_7(self):
        '''
        Valid Case: Assert EnglishCelex used by factory when language is 0 and version is 0
        '''
        language = 0
        language_str = "english"
        version = 0
        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = EnglishCelex
        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")

    def test_case_8(self):
        '''
        Valid Case: Assert EnglishCelex used by factory when language is 0 and version is 1
        '''
        language = 0
        language_str = "english"
        version = 1
        
        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = EnglishCelex

        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")
        self.assertEquals(version, obj.version, "Expected: " + str(version) + " Found: " + str(obj.version))
        self.assertEquals(language_str, obj.language, "Expected: " + language_str + " Found: " + str(obj.language))

    def test_case_9(self):
        '''
        Valid Case: Assert EnglishCelex used by factory when language is 0 and version is 2
        '''
        language = 0
        language_str = "english"
        version = 2
        
        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = EnglishCelex

        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")
        self.assertEquals(version, obj.version, "Expected: " + str(version) + " Found: " + str(obj.version))
        self.assertEquals(language_str, obj.language, "Expected: " + language_str + " Found: " + str(obj.language))

    def test_case_10(self):
        '''
        Valid Case: Assert GermanCelex used by factory when language is 1 and version is 0
        '''
        language = 1
        language_str = "german"
        version = 0
        
        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = GermanCelex
        
        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")
        self.assertEquals(version, obj.version, "Expected: " + str(version) + " Found: " + str(obj.version))
        self.assertEquals(language_str, obj.language, "Expected: " + language_str + " Found: " + str(obj.language))

    def test_case_11(self):
        '''
        Valid Case: Assert GermanCelex used by factory when language is 1 and version is 1
        '''
        language = 1
        language_str = "german"
        version = 1

        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = GermanCelex
        
        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")
        self.assertEquals(version, obj.version, "Expected: " + str(version) + " Found: " + str(obj.version))
        self.assertEquals(language_str, obj.language, "Expected: " + language_str + " Found: " + str(obj.language))

    def test_case_12(self):
        '''
        Valid Case: Assert GermanCelex used by factory when language is 1 and version is 2
        '''
        language = 1
        language_str = "german"
        version = 2

        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = GermanCelex
        
        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")
        self.assertEquals(version, obj.version, "Expected: " + str(version) + " Found: " + str(obj.version))
        self.assertEquals(language_str, obj.language, "Expected: " + language_str + " Found: " + str(obj.language))

    def test_case_13(self):
        '''
        Valid Case: Assert DutchCelex used by factory when language is 2 and version is 0
        '''
        language = 2
        language_str = "dutch"
        version = 0

        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = DutchCelex
        
        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")
        self.assertEquals(version, obj.version, "Expected: " + str(version) + " Found: " + str(obj.version))
        self.assertEquals(language_str, obj.language, "Expected: " + language_str + " Found: " + str(obj.language))

    def test_case_14(self):
        '''
        Valid Case: Assert DutchCelex used by factory when language is 2 and version is 1
        '''
        language = 2
        language_str = "dutch"
        version = 1

        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = DutchCelex
        
        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")
        self.assertEquals(version, obj.version, "Expected: " + str(version) + " Found: " + str(obj.version))
        self.assertEquals(language_str, obj.language, "Expected: " + language_str + " Found: " + str(obj.language))

    def test_case_15(self):
        '''
        Valid Case: Assert DutchCelex used by factory when language is 2 and version is 2
        '''
        language = 2
        language_str = "dutch"
        version = 2

        obj = build_celex(TEST_CELEX_PATH, language, version) 
        cls = DutchCelex
        
        self.assertIsInstance(obj, cls, "Language code " + str(language) + " should produce " + language_str + " celex")
        self.assertEquals(version, obj.version, "Expected: " + str(version) + " Found: " + str(obj.version))
        self.assertEquals(language_str, obj.language, "Expected: " + language_str + " Found: " + str(obj.language))

if __name__ == "__main__":
    unittest.main()