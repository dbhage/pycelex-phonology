'''
Created on Jun 11, 2014

@author: dbhage
'''

from celex import Celex

class DutchCelex(Celex):
    '''
    Dutch Celex
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.prefix = 'd'
        self.language = 'dutch'
        self.word_index = 1
        self.phon_index = 4        