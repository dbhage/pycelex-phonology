'''
Created on Jun 5, 2014

@author: dbhage
'''

from celex.factory.factory import build_celex

if __name__ == '__main__':
    celex_path = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/celex2/"
    language = 1
    version = 0
    celex = build_celex(celex_path, language, version)
    
    src_words_fname = "/home/dbhage/Dropbox/PiperLabDeanSharedFolder/PhonemeTranslations/Translated/GoetheMissingWords.csv"
    lines = open(src_words_fname, 'r').readlines()
    
    result = dict()
    for line in lines:
        word = line.replace('\n', '')
        result[word] = (celex.right_to_left(word), celex.left_to_right(word))

    output_fname = "/home/dbhage/piperlab/goethe_approximation_with_reslution.csv"

    open(output_fname, 'a').write("word,rtl,ltr\n")
    
    for (word, results) in result.items():
        line = word + ','
        
        for r in results:
            if (r is not None) and r!=[]:
                x = str(r)
                line += x.replace(',', ' ') + ','
            else:
                line += "NONE,"

        line = line[:len(line)-1]
        line += '\n'
        open(output_fname, 'a').write(line)