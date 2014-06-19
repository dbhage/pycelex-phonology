'''

Created on Mar 18, 2014

@author: dbhage

The classes required to build the celex dictionary.

'''

import os, re
from abc import ABCMeta

class Celex:
    '''
    Abstract class to be extended by classes implementing the 3 different celex dictionaries.
    '''
    __metaclass__ = ABCMeta
    
    def build(self, celex_path, version):
        '''
        Build the phoneme dict
        @param celex_path: the path to the celex2 main folder
        @param build_function: function to build the dictionary
        @postcondition: self.path, self.version and self.celex set
        '''
        self.path = celex_path + '/' + self.language + '/' + self.prefix + "pw" + '/' + self.prefix + "pw.cd"
        self.check_path()
        self.get_rows()
        
        if version == 0:
            self.build_dict_v0()    
        elif version == 1:
            self.build_dict_v1()
        elif version == 2:
            self.build_dict_v2()  

        self.version = version        

    def build_dict_v0(self):
        '''
        Build celex dictionary - V0
        A dict is built with words as keys and phoneme translations as values.
        The phoneme translation is a list with one element. That element holds the translation with any preceding apostrophe removed.
        @precondition: self.phon_index, self.word_index must have been assigned values. This is done in the constructor of the subclass. 
                       self.get_rows() must have been called so self.rows is assigned the proper value.
        @postcondition: self.celex is set
        '''
        phoneme_dict = dict()
        
        for row in self.rows:
            row = row.split('\\')
            phons = row[self.phon_index]
           
            # remove leading apostrophe
            if phons.startswith('\''):
                phons = [phons[1:]]
            else:
                phons = [phons]
                
            phoneme_dict[row[self.word_index].lower()] = phons
        
        self.celex = phoneme_dict
    
    def build_dict_v1(self):
        '''
        Build celex dictionary - V1
        A dict is built with words as keys and phoneme translations as values. 
        The phoneme translations has no preceding apostrophe and is split on hyphens.
        @precondition: self.phon_index, self.word_index must have been assigned values. This is done in the constructor of the subclass. 
                       self.get_rows() must have been called so self.rows is assigned the proper value.
        @postcondition: self.celex is set
        '''
        phoneme_dict = dict()
        
        for row in self.rows:
            row = row.split('\\')
            phons = row[self.phon_index]
           
            # remove leading apostrophe
            if phons.startswith('\''):
                phons = [phons[1:]]
            
            phons = ''.join(phons).split('-')
            phoneme_dict[row[self.word_index].lower()] = phons
        
        self.celex = phoneme_dict
    
    def build_dict_v2(self):
        '''
        Build celex dictionary - V2
        A dict is built with words as keys and phoneme translations as values. 
        The phoneme translations has no preceding apostrophe or any hyphens. Each element in the list is a character representing the phonetic symbols for that word.
        @precondition: self.phon_index, self.word_index must have been assigned values. This is done in the constructor of the subclass. 
                       self.get_rows() must have been called so self.rows is assigned the proper value.
        @postcondition: self.celex is set
        '''
        phoneme_dict = dict()
        
        for row in self.rows:
            row = row.split('\\')
            phons = row[self.phon_index]
           
            # remove leading apostrophe
            if phons.startswith('\''):
                phons = [phons[1:]]
            
            phons = list(re.sub(r"'|\"|-", '', ''.join(phons)))
            phoneme_dict[row[self.word_index].lower()] = phons
        
        self.celex = phoneme_dict

    def build_by_bigram(self):
        '''
        Build dictionary by indexing using the first bigrams of each word.
        @precondition: self.celex is set
        @postcondition: self.celex_by_bigram set
        '''
        celex_by_bigram = dict()
        
        for (k,v) in self.celex.items():
            if len(k) >= 2:
                if not k[:2] in celex_by_bigram:
                    celex_by_bigram[k[:2]] = dict()
                celex_by_bigram[k[:2]][k] = v
        
        self.celex_by_bigram = celex_by_bigram

    def check_path(self):
        '''
        Check if the path to celex2 exists
        @precondition: self.path must have been set
        '''
        if not os.path.exists(self.path):
            raise ValueError("Celex Path \'" + self.path + "\' does not exist.")
        
    def get_rows(self):
        '''
        Get rows from the file with words and phoneme translations
        @precondition: self.path must have been set
        @postcondition: self.rows set
        '''
        try:
            f = open(self.path, 'r')
            rows = f.readlines()
            f.close()
        except IOError:
            raise ValueError("Path for celex invalid.")
        self.rows = rows
        
    def __getitem__(self, word):
        '''
        Implementation of the indexing operator
        @precondition: self.celex dict must have been set
        @return: phoneme translation for word in the form of a list
        '''
        if word is None or word == '' or word not in self.celex:
            return None
        
        return self.celex[word]
        
    def __contains__(self, word):
        '''
        Implementation of the 'in' operator
        @return: True if word in self.celex, False otherwise
        '''
        return word in self.celex
        
    def right_to_left(self, word):
        '''
        Strip one letter at a time from the right and try to find a match in the remaining word in celex.
        If a match is found, remove the part of the word for which the match was found and then recurse
        to find a match for the remaining part of word.
        @param word: the word for which we need an approximate translation
        @precondition: self.celex must be set
        @return: an approximation for the word
        '''
        if len(word) > 1 and word in self.celex:
            print (word)
            return [(word, self.celex[word])]
        
        phoneme_translation = []
        
        for i in range(1, len(word)):
            current_word = word[:len(word)-i]
            if current_word in self.celex:
                if len(current_word) > 1: # don't want single letters to be translated
                    print (current_word)
                    phoneme_translation += [(current_word, self.celex[current_word])] + self.right_to_left(word[len(word)-i:])
                else:
                    phoneme_translation += self.right_to_left(word[len(word)-i:])
                break
        
        return phoneme_translation

    def left_to_right(self, word):
        '''
        Strip one letter at a time from the left and try to find a match in the remaining word in celex.
        If a match is found, remove the part of the word for which the match was found and then recurse
        to find a match for the remaining part of word.
        @precondition: self.celex must be set
        @return: an approximation for the word
        '''
        if len(word) > 1 and word in self.celex:
            print (word)
            return [(word, self.celex[word])]

        phoneme_translation = []
        
        for i in range(0, len(word)):
            current_word = word[i:]
            if current_word in self.celex:
                if len(current_word) > 1: # we don't want single letters to be translated
                    print (current_word)
                    phoneme_translation += self.left_to_right(word[:i]) + [(current_word, self.celex[current_word])]
                else:
                    phoneme_translation += self.left_to_right(word[:i])
                break

        return phoneme_translation
    
    def find_intersect(self, word):
        '''
        Find the smallest word which contains the required word
        @precondition: self.celex must be set
        @return: an approximation for the word
        '''
        if word in self.celex:
            return self.celex[word]

        smallest = None
        
        for (celex_word, phon_trans) in self.celex.items():
            if word in celex_word:
                if self.version == 0:
                    if smallest is None or len(phon_trans[0]) < len(smallest):
                        smallest = phon_trans[0]
                else:
                    if smallest is None or len(phon_trans) < len(smallest):
                        smallest = phon_trans

        return [smallest] if (smallest != None and self.version == 0) else smallest
    
    def levenshtein_approximation(self, word, levenshtein_function, threshold):
        '''
        Find the smallest word with levenshtein distance <threshold> of required word
        @param word: the word
        @param levenshtein_function: a function taking in 2 strings and returning an integer representing the levenshtein edit-distance between the 2 strings
        @param threshold: find words within levenshtein distance of threshold only
        @precondition: self.celex must be set
        @return: an approximation for the word
        '''
        if word in self.celex:
            return self.celex[word]

        smallest = None
        
        for (celex_word, phon_trans) in self.celex.items():
            if abs(len(celex_word) - len(word)) > threshold + 1:
                continue
                
            if levenshtein_function(word, celex_word) <= threshold:
                if self.version == 0:
                    if smallest is None or len(phon_trans[0]) < len(smallest):
                        smallest = phon_trans[0]
                else:
                    if smallest is None or len(phon_trans) < len(smallest):
                        smallest = phon_trans
        
        return [smallest] if (smallest != None and self.version == 0) else smallest