from nltk.corpus import wordnet as wn
import random
import ontologyGeneration as og

class Word(object):
    def __init__(self):
        self.word = ''
        self.domain_range = og.get_domain_range()
        self.domains = []
        # self.readDomains()
        # self.setRandomDomainHyponyms()

    # def readDomains(self):
    #     with open('D:\\master_2\\nlg_project\\list_nouns.txt', "r") as f:
    #         for line in f:
    #             self.domains.append(line.strip(' \t\n\r'))
    #
    # def setRandomDomainHyponyms(self):
    #     word_search_wordnet = (random.choice(self.domains))
    #     print(word_search_wordnet)
    #     self.discovered_hyponyms = wn.synset(word_search_wordnet + '.n.01').hyponyms()
    #
    # def getWordFromDomainHyponyms(self):
    #     hyponyms_choice = random.choice(self.discovered_hyponyms)
    #     return hyponyms_choice.lemma_names()[0]

    def domain_range(self):
        range_output_word = random.choice(self.domain_range)



