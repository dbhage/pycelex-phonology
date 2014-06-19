'''
Created on Jun 11, 2014

@author: dbhage
'''

from celex import Celex

class GermanCelex(Celex):
    '''
    German Celex
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        self.prefix = 'g'
        self.language = 'german'
        self.word_index = 1
        self.phon_index = 4