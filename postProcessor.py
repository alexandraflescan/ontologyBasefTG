from nltk.corpus import words
# test = "hgds" in words.words()
# print(test)

import inflect
import nltk.data

class PostProcessor():
    def __init__(self,text):
        self.text = text
    def capitalise_words(self):
         sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
         sentences = sent_tokenizer.tokenize(self.text)
         sentences = [sent.capitalize() for sent in sentences]
         self.text = ' '.join(sentences)
         return self
