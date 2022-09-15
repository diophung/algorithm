import requests
from urllib import request


class JottoGameSolver:

    def get_english_words(self):
        """
        Returns a list of all 279496 valid words:
        ['AA', 'AAH', 'AAHED', ... 'ZYZZYVAS', 'ZZZ', 'ZZZS']
        """
        words_url = 'http://www.raphey.com/gd/words.txt'
        # or get from /usr/share/dict/words
        return [str(line.strip(), 'utf-8') for line in request.urlopen(words_url)]


    """
    Test required
    """

    def get_secret_word(self, guesses_and_match_counts: list[tuple[str, int]]):
        """
        Missing summary--what is this doing?
        1. filter word list down to only correct-length words
        2. ???

        Returns:

        """
        ws = self.get_english_words()  # ws --> same_length_words
        new_ws = []
        for w in ws:
            if len(w) == len(guesses_and_match_counts[0][0]):
                new_ws.append(w)
        ws = new_ws

        # loop through all guesses,
        # compare each word in the filter sets against the guess,
        # if the word meets the constraint, add it to the output

        for guess, count in guesses_and_match_counts:
            new_ws = []
            for w in ws:
                n_matches = 0  #
                for c in range(len(guess)):
                    if guess[c] == w[c]:
                        n_matches += 1
                if n_matches == count:
                    new_ws.append(w)
            ws = new_ws
        return ws


sample_case_0 = [('TIGER', 0), ('GOOSE', 3), ('MOOSE', 4), ('HORSE', 3)]  # MOUSE
sample_case_1 = [('HEAD', 0), ('NECK', 1), ('KNEE', 1), ('FOOT', 1), ('FACE', 1), ('LASH', 1)]  # NOSE
sample_case_2 = [('POTATO', 3), ('CELERY', 2), ('TURKEY', 0), ('PAPAYA', 1)]  # GELATO

sln = JottoGameSolver()
print(sln.get_secret_word(sample_case_0))
print(sln.get_secret_word(sample_case_1))
print(sln.get_secret_word(sample_case_2))
