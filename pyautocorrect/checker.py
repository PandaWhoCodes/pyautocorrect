import re, collections, os


class check():
    def get_words(self, text):
        return re.findall('[a-z]+', text.lower())

    def langModel(self, wordseq):
        wordCount = collections.defaultdict(lambda: 1)
        for word in wordseq:
            wordCount[word] += 1
        return wordCount

    def set_constants(self):
        PATH = os.path.abspath(os.path.dirname(__file__))
        shakespeare = os.path.join(PATH, "shakespeare.txt")
        with open(shakespeare, "r") as f:
            self.file = f.read()
        self.dictionary = self.langModel(self.get_words(self.file))
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def dist1_words(self, word):
        """
        An adaptation of Peter Norvig's spell corrector
        """
        splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        deletes = [a + b[1:] for a, b in splits if b]  # n deletions
        transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b) > 1]  # n-1 transpositions
        replaces = [a + c + b[1:] for a, b in splits for c in self.alphabets if b]  # 26n alterations
        inserts = [a + c + b for a, b in splits for c in self.alphabets]  # 26(n+1) insertions
        return set(deletes + transposes + replaces + inserts)

    def dist2_words(self, word):
        return set(word2 for word1 in self.dist1_words(word) for word2 in self.dist1_words(word1))

    def legal_words(self, words):
        return set(w for w in words if w in self.dictionary)

    def correct_word(self, word):
        possibleWords = self.legal_words([word]) or self.legal_words(self.dist1_words(word)) or self.legal_words(
            self.dist2_words(word)) or [word]
        return max(possibleWords, key=self.dictionary.get)

    def correct_words(self, sentence):
        words = self.get_words(sentence)
        return ' '.join(self.correct_word(word) for word in words)
