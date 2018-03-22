import lemmagen.lemmatizer
from lemmagen.lemmatizer import Lemmatizer
from bs4 import BeautifulSoup as bs
import re
from nltk import word_tokenize
#tree = ET.parse('AGIF_small.tmx')
#root = tree.getroot()


def get_lemmas(strings, lemmatizer):
    result = []
    for string in strings:
        string = word_tokenize(string)
        lstring = [lemmatizer.lemmatize(x) for x in string]
        string = " ".join(lstring)
        result.append(string)
    return result
        

sl = []
en = []

with open('AGIF_small.tmx') as fp:
    xml = bs(fp, 'lxml-xml')
    for cnt, tuv in enumerate(xml.body.find_all('tuv')):
        if tuv.get('xml:lang') == 'en-GB':
            text = tuv.seg.getText().replace('\\n', ' ').replace('\n', ' ').replace('\u2028', ' ').replace('\t', ' ').strip()
            text = re.sub('\\.+', '.', text)
            text = ' '.join(text.split()).lower()
            en.append(text)
        elif tuv.get('xml:lang') == 'sl-SI':
            text = tuv.seg.getText().replace('\\n', ' ').replace('\n', ' ').replace('\u2028', ' ').replace('\t', ' ').strip()
            text = re.sub('\\.+', '.', text)
            text = ' '.join(text.split()).lower()
            sl.append(text)
            
        
        
lemmatizer_en = Lemmatizer(dictionary=lemmagen.DICTIONARY_ENGLISH)
lemmatizer_sl = Lemmatizer(dictionary=lemmagen.DICTIONARY_SLOVENE)

sl_lemmas = get_lemmas(sl, lemmatizer_sl)

for el in sl_lemmas:
    print(el)
