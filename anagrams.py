# An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.[1] For example, the word anagram can be rearranged into nag a ram, or the word binary into brainy or the word adobe into abode.

class Anagram(object):
    def __init__(self):
        self.dict = self.build_dict()

    def build_dict(self):
        """"Build a dictionary"""
        dict = {}
        word_list = open("/usr/share/dict/words", "r").readlines()
        for word in word_list:
            word = word.strip().lower()
            words = ''.join(sorted(word))
            dict[words] = word
        return dict

    def unscramble(self, words):
        """Unscramble the letters"""
        for word in words:
            word_sorted = ''.join(sorted(word))
            if word_sorted in self.dict:
                print(self.dict[word_sorted])

if __name__ == '__main__':
# good:
    words = ['tacocat', 'amnesia']
    jumble = Anagram()
    jumble.unscramble(words)

    words = ['catholic', 'urn']
    jumble = Anagram()
    jumble.unscramble(words)

# edge:
    words = ['listen', 'google']
    jumble = Anagram()
    jumble.unscramble(words)

    words = ['asdasdcast', 'dasdaoh']
    jumble = Anagram()
    jumble.unscramble(words)

# bad:
    words = [10, 11, 12, 13]
    jumble = Anagram()
    jumble.unscramble(words)

    words = [1, 5, 10, 25]
    jumble = Anagram()
    jumble.unscramble(words)
