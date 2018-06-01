import random
class Dictionary:
    def __init__(self):
        self.addition_verbs = self.read('addition_verbs.txt')
        self.subtraction_verbs = self.read('subtraction_verbs.txt')
        self.multiplication_verbs = self.read('multiplication_verbs.txt')
        self.division_verbs = self.read('division_verbs.txt')

    def read(self, filename):
        words = []
        with open(filename, "r") as f:
            for line in f:
                words.append(line.strip(' \t\n\r'))

        return words






