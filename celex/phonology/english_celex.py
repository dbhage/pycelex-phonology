'''
Created on Jun 11, 2014

@author: dbhage
'''

from celex import Celex

class EnglishCelex(Celex):
    '''
    English Celex
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.prefix = 'e'
        self.language = 'english'
        self.word_index = 1
        self.phon_index = 6
