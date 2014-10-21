'''
Created on Jun 2, 2014

@author: dbhage

Factory to create Celex objects
'''

import os

from celex.phonology.english_celex import EnglishCelex
from celex.phonology.dutch_celex import DutchCelex
from celex.phonology.german_celex import GermanCelex

def build_celex(celex_path, language, version):
    '''
    Build the Celex2 dictionary.
    Phoneme translations will always be returned as a list - See version for format.
    
    @param celex_path: Path to the celex2 directory
    @type celex_path: str
    
    @param language: 0 - English, 1 - German, 2 - Dutch
    @type language: int
    
    @param version: 0 - leading apostrophe removed, 1 - split on hyphens, 2 - all characters listed separately
    @type version: int
    
    @return: Celex object built according to parameters passed
    @rtype: Celex obj
    
    @raise ValueError: raises ValueError if celex_path parameter is invalid or language or version out of range
    '''
    check_path(celex_path)

    if language not in [0,1,2]:
        raise ValueError("Language not in range. Expected 0, 1 or 2, Found:" + str(language))

    if version not in [0,1,2]:
        raise ValueError("Version not in range. Expected 0, 1 or 2, Found:" + str(version))

    if language == 0:
        celex = EnglishCelex()
    elif language == 1:
        celex = GermanCelex()
    else:
        celex = DutchCelex()
    
    celex.build(celex_path, version)
    
    return celex

def check_path(celex_path):
    '''
    Check if the path to celex2 exists
    
    @param celex_path: the path to the celex2 root directory
    @type celex_path: str
    
    @raise ValueError: raised if celex_path does not exist
    '''
    if not os.path.exists(celex_path):
        raise ValueError("Celex Path \'" + celex_path + "\' does not exist.")