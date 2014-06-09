'''
Created on Jun 9, 2014

@author: dbhage

English Celex Test Suite

'''

import unittest

from celex.celex import EnglishCelex 
from test import TEST_CELEX_PATH

class EnglishCelexTest(unittest.TestCase):

    def setUp(self):
        '''
        Set values for tests.
        '''
        self.expected_prefix = 'e'
        self.expected_language = "english"
        self.expected_word_index = 1
        self.expected_phon_index = 6

        self.invalid_path = "invalid_path/"
        self.cls = EnglishCelex

        self.expected_dict_v0 = {'abilities': ["@-'bI-l@-tIz"], 
                                 'abdications': ['"{b-dI-\'k1-SHz'], 
                                 'abbreviation': ['@-"bri-vI-\'1-SH'], 
                                 'abatement': ["@-'b1t-m@nt"], 
                                 'abbreviate': ["@-'bri-vI-1t"], 
                                 'abettor': ["@-'bE-t@R"], 
                                 'abducts': ["@b-'dVkts"], 
                                 'abbes': ['{-b1z'], 
                                 'abhorred': ["@b-'h$d"], 
                                 'abbey': ['{-bI'], 
                                 'abhorrent': ["@b-'hQ-r@nt"], 
                                 'abiding': ["@-'b2-dIN"], 
                                 'abeyant': ["@-'b1-@nt"], 
                                 'abbe': ['{-b1'], 
                                 'abashed': ["@-'b{St"], 
                                 'abandons': ["@-'b{n-d@nz"], 
                                 'abashes': ["@-'b{-SIz"], 
                                 'abduction': ["{b-'dVk-SH"], 
                                 'abacus': ['{-b@-k@s'], 
                                 'abhorrence': ["@b-'hQ-r@ns"], 
                                 'abed': ["@-'bEd"], 
                                 'abaft': ["@-'b#ft"], 
                                 'abattoirs': ['{-b@-tw#z'], 
                                 'abbreviated': ["@-'bri-vI-1-tId"], 
                                 'abetting': ["@-'bE-tIN"], 
                                 'abbreviates': ["@-'bri-vI-1ts"], 
                                 'ability': ["@-'bI-l@-tI"], 
                                 'abdication': ['"{b-dI-\'k1-SH'], 
                                 'abc': ['"1-bi-\'si'], 
                                 'abetted': ["@-'bE-tId"], 
                                 'abide': ["@-'b2d"], 
                                 'abided by': ["@-'b2-dId-b2"], 
                                 'abides': ["@-'b2dz"], 
                                 'abhorring': ["@b-'h$-rIN"], 
                                 'abbots': ['{-b@ts'], 
                                 'aberration': ['"{-b@-\'r1-SH'], 
                                 'abdicated': ['{b-dI-k1-tId'], 
                                 'abbess': ['{-bEs'], 
                                 'abdicates': ['{b-dI-k1ts'], 
                                 'abbreviating': ["@-'bri-vI-1-tIN"], 
                                 'abasement': ["@-'b1s-m@nt"], 
                                 'abets': ["@-'bEts"], 
                                 'abet': ["@-'bEt"], 
                                 'abbesses': ['{-bE-sIz'], 
                                 'abeyance': ["@-'b1-@ns"], 
                                 'abattoir': ['{-b@-tw#R'], 
                                 'abash': ["@-'b{S"], 
                                 'aberrant': ["{-'bE-r@nt"], 
                                 'abase': ["@-'b1s"], 
                                 'aback': ["@-'b{k"], 
                                 'abaci': ['{-b@-s2'], 
                                 'abdominal': ["{b-'dQ-mI-nP"], 
                                 'abbreviations': ['@-"bri-vI-\'1-SHz'], 
                                 'abate': ["@-'b1t"], 
                                 'abbeys': ['{-bIz'], 
                                 'abating': ["@-'b1-tIN"], 
                                 'abiding by': ["@-'b2-dIN-b2"], 
                                 'abductions': ["{b-'dVk-SHz"], 
                                 'abates': ["@-'b1ts"], 
                                 'abated': ["@-'b1-tId"], 
                                 'abduct': ["@b-'dVkt"], 
                                 "abc's": ['"1-bi-\'siz'], 
                                 'abasing': ["@-'b1-sIN"], 
                                 'abandoned': ["@-'b{n-d@nd"], 
                                 'abeam': ["@-'bim"], 
                                 'abdicating': ['{b-dI-k1-tIN'], 
                                 'abacuses': ['{-b@-k@-sIz'], 
                                 'aas': ['"1-\'1z'], 
                                 'abandon': ["@-'b{n-d@n"], 
                                 'abducted': ["@b-'dVk-tId"], 
                                 'aa': ['"1-\'1'], 
                                 'abandonment': ["@-'b{n-d@n-m@nt"], 
                                 'abashing': ["@-'b{-SIN"], 
                                 'abducting': ["@b-'dVk-tIN"], 
                                 'abbot': ['{-b@t'], 
                                 'abcs': ['"1-bi-\'siz'], 
                                 'abhors': ["@b-'h$z"], 
                                 'abdomens': ['{b-d@-mEnz'], 
                                 'abased': ["@-'b1st"], 
                                 'abide by': ["@-'b2d-b2"], 
                                 'abases': ["@-'b1-sIz"], 
                                 'abidance by': ['@-\'b2-d@ns-"b2'], 
                                 'abdicate': ['{b-dI-k1t'], 
                                 'abandoning': ["@-'b{n-d@-nIN"], 
                                 'abdomen': ['{b-d@-mEn'], 
                                 'abides by': ["@-'b2dz-b2"], 
                                 'abided': ["@-'b2-dId"], 
                                 'abettors': ["@-'bE-t@z"], 
                                 'aberrations': ['"{-b@-\'r1-SHz'], 
                                 'a': ['1'], 
                                 'abhor': ["@b-'h$R"]}
        
        self.expected_dict_v1 = {'abilities': ['@', "'bI", 'l@', 'tIz'],
                                'abdications': ['"{b', 'dI', "'k1", 'SHz'],
                                'abbreviation': ['@', '"bri', 'vI', "'1", 'SH'],
                                'abatement': ['@', "'b1t", 'm@nt'],
                                'abbreviate': ['@', "'bri", 'vI', '1t'],
                                'abettor': ['@', "'bE", 't@R'],
                                'abducts': ['@b', "'dVkts"],
                                'abbes': ['{', 'b1z'],
                                'abhorred': ['@b', "'h$d"],
                                'abbey': ['{', 'bI'],
                                'abhorrent': ['@b', "'hQ", 'r@nt'],
                                'abiding': ['@', "'b2", 'dIN'],
                                'abeyant': ['@', "'b1", '@nt'],
                                'abbe': ['{', 'b1'],
                                'abashed': ['@', "'b{St"],
                                'abandons': ['@', "'b{n", 'd@nz'],
                                'abashes': ['@', "'b{", 'SIz'],
                                'abduction': ['{b', "'dVk", 'SH'],
                                'abacus': ['{', 'b@', 'k@s'],
                                'abhorrence': ['@b', "'hQ", 'r@ns'],
                                'abed': ['@', "'bEd"],
                                'abaft': ['@', "'b#ft"],
                                'abattoirs': ['{', 'b@', 'tw#z'],
                                'abbreviated': ['@', "'bri", 'vI', '1', 'tId'],
                                'abetting': ['@', "'bE", 'tIN'],
                                'abbreviates': ['@', "'bri", 'vI', '1ts'],
                                'ability': ['@', "'bI", 'l@', 'tI'],
                                'abdication': ['"{b', 'dI', "'k1", 'SH'],
                                'abc': ['"1', 'bi', "'si"],
                                'abetted': ['@', "'bE", 'tId'],
                                'abide': ['@', "'b2d"],
                                'abided by': ['@', "'b2", 'dId', 'b2'],
                                'abides': ['@', "'b2dz"],
                                'abhorring': ['@b', "'h$", 'rIN'],
                                'abbots': ['{', 'b@ts'],
                                'aberration': ['"{', 'b@', "'r1", 'SH'],
                                'abdicated': ['{b', 'dI', 'k1', 'tId'],
                                'abbess': ['{', 'bEs'],
                                'abdicates': ['{b', 'dI', 'k1ts'],
                                'abbreviating': ['@', "'bri", 'vI', '1', 'tIN'],
                                'abasement': ['@', "'b1s", 'm@nt'],
                                'abets': ['@', "'bEts"],
                                'abet': ['@', "'bEt"],
                                'abbesses': ['{', 'bE', 'sIz'],
                                'abeyance': ['@', "'b1", '@ns'],
                                'abattoir': ['{', 'b@', 'tw#R'],
                                'abash': ['@', "'b{S"],
                                'aberrant': ['{', "'bE", 'r@nt'],
                                'abase': ['@', "'b1s"],
                                'aback': ['@', "'b{k"],
                                'abaci': ['{', 'b@', 's2'],
                                'abdominal': ['{b', "'dQ", 'mI', 'nP'],
                                'abbreviations': ['@', '"bri', 'vI', "'1", 'SHz'],
                                'abate': ['@', "'b1t"],
                                'abbeys': ['{', 'bIz'],
                                'abating': ['@', "'b1", 'tIN'],
                                'abiding by': ['@', "'b2", 'dIN', 'b2'],
                                'abductions': ['{b', "'dVk", 'SHz'],
                                'abates': ['@', "'b1ts"],
                                'abated': ['@', "'b1", 'tId'],
                                'abduct': ['@b', "'dVkt"],
                                "abc's": ['"1', 'bi', "'siz"],
                                'abasing': ['@', "'b1", 'sIN'],
                                'abandoned': ['@', "'b{n", 'd@nd'],
                                'abeam': ['@', "'bim"],
                                'abdicating': ['{b', 'dI', 'k1', 'tIN'],
                                'abacuses': ['{', 'b@', 'k@', 'sIz'],
                                'aas': ['"1', "'1z"],
                                'abandon': ['@', "'b{n", 'd@n'],
                                'abducted': ['@b', "'dVk", 'tId'],
                                'aa': ['"1', "'1"],
                                'abandonment': ['@', "'b{n", 'd@n', 'm@nt'],
                                'abashing': ['@', "'b{", 'SIN'],
                                'abducting': ['@b', "'dVk", 'tIN'],
                                'abbot': ['{', 'b@t'],
                                'abcs': ['"1', 'bi', "'siz"],
                                'abhors': ['@b', "'h$z"],
                                'abdomens': ['{b', 'd@', 'mEnz'],
                                'abased': ['@', "'b1st"],
                                'abide by': ['@', "'b2d", 'b2'],
                                'abases': ['@', "'b1", 'sIz'],
                                'abidance by': ['@', "'b2", 'd@ns', '"b2'],
                                'abdicate': ['{b', 'dI', 'k1t'],
                                'abandoning': ['@', "'b{n", 'd@', 'nIN'],
                                'abdomen': ['{b', 'd@', 'mEn'],
                                'abides by': ['@', "'b2dz", 'b2'],
                                'abided': ['@', "'b2", 'dId'],
                                'abettors': ['@', "'bE", 't@z'],
                                'aberrations': ['"{', 'b@', "'r1", 'SHz'],
                                'a': ['1'],
                                'abhor': ['@b', "'h$R"]}
 
        self.expected_dict_v2 = {'abilities': ['@', 'b', 'I', 'l', '@', 't', 'I', 'z'],
                                'abdications': ['{', 'b', 'd', 'I', 'k', '1', 'S', 'H', 'z'],
                                'abbreviation': ['@', 'b', 'r', 'i', 'v', 'I', '1', 'S', 'H'],
                                'abatement': ['@', 'b', '1', 't', 'm', '@', 'n', 't'],
                                'abbreviate': ['@', 'b', 'r', 'i', 'v', 'I', '1', 't'],
                                'abettor': ['@', 'b', 'E', 't', '@', 'R'],
                                'abducts': ['@', 'b', 'd', 'V', 'k', 't', 's'],
                                'abbes': ['{', 'b', '1', 'z'],
                                'abhorred': ['@', 'b', 'h', '$', 'd'],
                                'abbey': ['{', 'b', 'I'],
                                'abhorrent': ['@', 'b', 'h', 'Q', 'r', '@', 'n', 't'],
                                'abiding': ['@', 'b', '2', 'd', 'I', 'N'],
                                'abeyant': ['@', 'b', '1', '@', 'n', 't'],
                                'abbe': ['{', 'b', '1'],
                                'abashed': ['@', 'b', '{', 'S', 't'],
                                'abandons': ['@', 'b', '{', 'n', 'd', '@', 'n', 'z'],
                                'abashes': ['@', 'b', '{', 'S', 'I', 'z'],
                                'abduction': ['{', 'b', 'd', 'V', 'k', 'S', 'H'],
                                'abacus': ['{', 'b', '@', 'k', '@', 's'],
                                'abhorrence': ['@', 'b', 'h', 'Q', 'r', '@', 'n', 's'],
                                'abed': ['@', 'b', 'E', 'd'],
                                'abaft': ['@', 'b', '#', 'f', 't'],
                                'abattoirs': ['{', 'b', '@', 't', 'w', '#', 'z'],
                                'abbreviated': ['@', 'b', 'r', 'i', 'v', 'I', '1', 't', 'I', 'd'],
                                'abetting': ['@', 'b', 'E', 't', 'I', 'N'],
                                'abbreviates': ['@', 'b', 'r', 'i', 'v', 'I', '1', 't', 's'],
                                'ability': ['@', 'b', 'I', 'l', '@', 't', 'I'],
                                'abdication': ['{', 'b', 'd', 'I', 'k', '1', 'S', 'H'],
                                'abc': ['1', 'b', 'i', 's', 'i'],
                                'abetted': ['@', 'b', 'E', 't', 'I', 'd'],
                                'abide': ['@', 'b', '2', 'd'],
                                'abided by': ['@', 'b', '2', 'd', 'I', 'd', 'b', '2'],
                                'abides': ['@', 'b', '2', 'd', 'z'],
                                'abhorring': ['@', 'b', 'h', '$', 'r', 'I', 'N'],
                                'abbots': ['{', 'b', '@', 't', 's'],
                                'aberration': ['{', 'b', '@', 'r', '1', 'S', 'H'],
                                'abdicated': ['{', 'b', 'd', 'I', 'k', '1', 't', 'I', 'd'],
                                'abbess': ['{', 'b', 'E', 's'],
                                'abdicates': ['{', 'b', 'd', 'I', 'k', '1', 't', 's'],
                                'abbreviating': ['@', 'b', 'r', 'i', 'v', 'I', '1', 't', 'I', 'N'],
                                'abasement': ['@', 'b', '1', 's', 'm', '@', 'n', 't'],
                                'abets': ['@', 'b', 'E', 't', 's'],
                                'abet': ['@', 'b', 'E', 't'],
                                'abbesses': ['{', 'b', 'E', 's', 'I', 'z'],
                                'abeyance': ['@', 'b', '1', '@', 'n', 's'],
                                'abattoir': ['{', 'b', '@', 't', 'w', '#', 'R'],
                                'abash': ['@', 'b', '{', 'S'],
                                'aberrant': ['{', 'b', 'E', 'r', '@', 'n', 't'],
                                'abase': ['@', 'b', '1', 's'],
                                'aback': ['@', 'b', '{', 'k'],
                                'abaci': ['{', 'b', '@', 's', '2'],
                                'abdominal': ['{', 'b', 'd', 'Q', 'm', 'I', 'n', 'P'],
                                'abbreviations': ['@', 'b', 'r', 'i', 'v', 'I', '1', 'S', 'H', 'z'],
                                'abate': ['@', 'b', '1', 't'],
                                'abbeys': ['{', 'b', 'I', 'z'],
                                'abating': ['@', 'b', '1', 't', 'I', 'N'],
                                'abiding by': ['@', 'b', '2', 'd', 'I', 'N', 'b', '2'],
                                'abductions': ['{', 'b', 'd', 'V', 'k', 'S', 'H', 'z'],
                                'abates': ['@', 'b', '1', 't', 's'],
                                'abated': ['@', 'b', '1', 't', 'I', 'd'],
                                'abduct': ['@', 'b', 'd', 'V', 'k', 't'],
                                "abc's": ['1', 'b', 'i', 's', 'i', 'z'],
                                'abasing': ['@', 'b', '1', 's', 'I', 'N'],
                                'abandoned': ['@', 'b', '{', 'n', 'd', '@', 'n', 'd'],
                                'abeam': ['@', 'b', 'i', 'm'],
                                'abdicating': ['{', 'b', 'd', 'I', 'k', '1', 't', 'I', 'N'],
                                'abacuses': ['{', 'b', '@', 'k', '@', 's', 'I', 'z'],
                                'aas': ['1', '1', 'z'],
                                'abandon': ['@', 'b', '{', 'n', 'd', '@', 'n'],
                                'abducted': ['@', 'b', 'd', 'V', 'k', 't', 'I', 'd'],
                                'aa': ['1', '1'],
                                'abandonment': ['@', 'b', '{', 'n', 'd', '@', 'n', 'm', '@', 'n', 't'],
                                'abashing': ['@', 'b', '{', 'S', 'I', 'N'],
                                'abducting': ['@', 'b', 'd', 'V', 'k', 't', 'I', 'N'],
                                'abbot': ['{', 'b', '@', 't'],
                                'abcs': ['1', 'b', 'i', 's', 'i', 'z'],
                                'abhors': ['@', 'b', 'h', '$', 'z'],
                                'abdomens': ['{', 'b', 'd', '@', 'm', 'E', 'n', 'z'],
                                'abased': ['@', 'b', '1', 's', 't'],
                                'abide by': ['@', 'b', '2', 'd', 'b', '2'],
                                'abases': ['@', 'b', '1', 's', 'I', 'z'],
                                'abidance by': ['@', 'b', '2', 'd', '@', 'n', 's', 'b', '2'],
                                'abdicate': ['{', 'b', 'd', 'I', 'k', '1', 't'],
                                'abandoning': ['@', 'b', '{', 'n', 'd', '@', 'n', 'I', 'N'],
                                'abdomen': ['{', 'b', 'd', '@', 'm', 'E', 'n'],
                                'abides by': ['@', 'b', '2', 'd', 'z', 'b', '2'],
                                'abided': ['@', 'b', '2', 'd', 'I', 'd'],
                                'abettors': ['@', 'b', 'E', 't', '@', 'z'],
                                'aberrations': ['{', 'b', '@', 'r', '1', 'S', 'H', 'z'],
                                'a': ['1'],
                                'abhor': ['@', 'b', 'h', '$', 'R']}
        
        self.non_existing_word = "dean"
 
    def test_case_1(self):
        '''
        Test constructor
        '''
        celex = EnglishCelex()
        self.assertEqual(self.expected_prefix, celex.prefix, "Expected: " + self.expected_prefix + ", Found: " + celex.prefix)
        self.assertEqual(self.expected_language, celex.language, "Expected: " + self.expected_language + ", Found: " + celex.language)
        self.assertEqual(self.expected_word_index, celex.word_index, "Expected: " + str(self.expected_word_index) + ", Found: " + str(celex.word_index))
        self.assertEqual(self.expected_phon_index, celex.phon_index, "Expected: " + str(self.expected_phon_index) + ", Found: " + str(celex.phon_index))

    def test_case_2(self):
        '''
        Invalid case: Set self.path to an invalid path and then check if self.check_path throws a ValueError exception
        '''
        celex = self.cls()
        celex.path = self.invalid_path
        self.assertRaises(ValueError, celex.check_path)
    
    def test_case_3(self):
        '''
        Valid case: Set self.path to a valid path and then make sure self.check_path does not throw any exception
        '''
        celex = self.cls()
        celex.path = TEST_CELEX_PATH
        try:
            celex.check_path()
        except ValueError:
            self.fail("ValueError exception thrown for valid path.")        

    def test_case_4(self):
        '''
        Valid case: test Celex.build_dict_v0
        '''
        celex = self.cls()
        celex.path = TEST_CELEX_PATH + '/' + self.expected_language + '/' + self.expected_prefix + "pw" + '/' + self.expected_prefix + "pw.cd"
        celex.get_rows()
        celex.build_dict_v0()
        
        for phoneme_translations in celex.celex.values():
            self.assertEqual(len(phoneme_translations), 1, "In version 0, all lists for phoneme translations must have length 1.")

        self.assertEquals(self.expected_dict_v0, celex.celex, "Expected dict and actual dict do not match.")

    def test_case_5(self):
        '''
        Valid case: test Celex.build_dict_v1
        '''
        celex = self.cls()
        celex.path = TEST_CELEX_PATH + '/' + self.expected_language + '/' + self.expected_prefix + "pw" + '/' + self.expected_prefix + "pw.cd"
        celex.get_rows()
        celex.build_dict_v1()
        
        self.assertEquals(self.expected_dict_v1, celex.celex, "Expected dict and actual dict do not match.")

    def test_case_6(self):
        '''
        Valid case: test Celex.build_dict_v2
        '''
        celex = self.cls()
        celex.path = TEST_CELEX_PATH + '/' + self.expected_language + '/' + self.expected_prefix + "pw" + '/' + self.expected_prefix + "pw.cd"
        celex.get_rows()
        celex.build_dict_v2()
        
        self.assertEquals(self.expected_dict_v2, celex.celex, "Expected dict and actual dict do not match.")

    def test_case_7(self):
        '''
        Invalid Case: Test indexing operator with non-existing word
        '''
        celex = self.cls()
        celex.celex = {"abc": "ABC",
                       "pol": "POL"}
        
        self.assertIsNone(celex[self.non_existing_word], "")

    def test_case_8(self):
        '''
        Invalid Case: Test indexing operator with empty string
        '''
        celex = self.cls()
        celex.celex = {"abc": "ABC",
                       "pol": "POL"}
        
        self.assertIsNone(celex[''], "")

    def test_case_9(self):
        '''
        Invalid Case: Test indexing operator with None
        '''
        celex = self.cls()
        celex.celex = {"abc": "ABC",
                       "pol": "POL"}
        
        self.assertIsNone(celex[None], "")
    
    def test_case_10(self):
        '''
        Valid Case: Test indexing operator with existing word
        '''
        celex = self.cls()
        celex.celex = {"abc": "ABC",
                       "pol": "POL"}
        
        self.assertEquals("ABC", celex["abc"], "Expected: ABC, Found: " + celex["abc"])

    def test_case_11(self):
        '''
        Invalid case: test contains operator with non existing word
        '''
        celex = self.cls()
        celex.celex = {"abc": "ABC",
                       "pol": "POL"}
        
        self.assertFalse(self.non_existing_word in celex, "Non existing word found in celex.")
    
    def test_case_12(self):
        '''
        Invalid Case: Test contains operator with empty string
        '''
        celex = self.cls()
        celex.celex = {"abc": "ABC",
                       "pol": "POL"}
        
        self.assertFalse('' in celex, "Empty string should not be in celex.")

    def test_case_13(self):
        '''
        Invalid Case: Test indexing operator with None
        '''
        celex = self.cls()
        celex.celex = {"abc": "ABC",
                       "pol": "POL"}
        
        self.assertFalse(None in celex, "None should not be in celex.")

    def test_case_14(self):
        '''
        Valid Case: test contains operator with existing word
        '''
        celex = self.cls()
        celex.celex = {"abc": "ABC",
                       "pol": "POL"}
        
        self.assertTrue("pol" in celex, "Existing word not found in celex.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_case_1']
    unittest.main()