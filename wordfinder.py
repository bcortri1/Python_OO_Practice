"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, filename):
            self.file = open(filename, "r")
            self.wordlist = [word.strip() for word in self.file.readlines()]
            self.file.close()
    def random(self):
        from random import randrange as rand
        return self.wordlist[rand(0,len(self.wordlist))]

class SpecialWordFinder(WordFinder):
    def __init__(self, filename):
        super().__init__(self, filename)
        self.wordlist = [word for word in self.wordlist if word[0] != "#"]
