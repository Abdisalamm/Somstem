#The main class call the rules and try stemming somali words.
#The core idea in this script is to show how to call and use the created stemmer in an other class.
import nltk
nltk.download('punkt_tab')   #We add NLTK
from nltk.tokenize import word_tokenize
from Somstem.Somali import SomStemmerImpl
import re
import nltk
stemmer = SomStemmerImpl()

while True:
    input_word = input("Enter a word to stem: ")
    if input_word.lower() == 'bax':
        print("Nabad galiyo")
        break
    words = word_tokenize(input_word)
    my_stemmed_word = []
    for word in words:
        processed_word = re.sub(r'^[^a-zA-Z]+|[^a-zA-Z]+$', '', word.lower())
        stemmed_word = stemmer.somstem( processed_word)
        my_stemmed_word.append(stemmed_word)
    print("Stemmed words:", my_stemmed_word)