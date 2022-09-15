import requests
from urllib import request
import unittest


class JottoGameSolver:

    def get_english_words(self):
        """
        Returns a list of all 279496 valid words:
        ['AA', 'AAH', 'AAHED', ... 'ZYZZYVAS', 'ZZZ', 'ZZZS']
        """
        words_url = 'http://www.raphey.com/gd/words.txt'
        # or get from /usr/share/dict/words
        return [str(line.strip(), 'utf-8') for line in request.urlopen(words_url)]

    def get_secret_word(self, guesses_and_match_counts: list[tuple[str, int]]):
        """
        To find the secret word, given the list of guesses.
        Each guess is represented by a tuple: (word, match_count)
            word: the guessed English word
            match_count: the number of character that matches (both index and value)

        Returns:
            a single English word that satisfies every condition in the list of guessed words
        """
        english_words = self.get_english_words()  # ws --> same_length_words
        new_words = []
        for word in english_words:
            if len(word) == len(guesses_and_match_counts[0][0]):
                new_words.append(word)
        english_words = new_words

        # loop through all guesses,
        # compare each word in the filter sets against the guess,
        # if the word meets the constraint, then add it to the output
        for guessed_word, count in guesses_and_match_counts:
            new_words = []
            for word in english_words:
                number_of_matches = 0  #
                for c in range(len(guessed_word)):
                    if guessed_word[c] == word[c]:
                        number_of_matches += 1
                if number_of_matches == count:
                    new_words.append(word)
            english_words = new_words
        return english_words[0]


class JottoGameSolverTest(unittest.TestCase):

    def test_positive_case(self):
        sample_case_0 = [('TIGER', 0), ('GOOSE', 3), ('MOOSE', 4), ('HORSE', 3)]  # MOUSE
        sample_case_1 = [('HEAD', 0), ('NECK', 1), ('KNEE', 1), ('FOOT', 1), ('FACE', 1), ('LASH', 1)]  # NOSE
        sample_case_2 = [('POTATO', 3), ('CELERY', 2), ('TURKEY', 0), ('PAPAYA', 1)]  # GELATO

        sln = JottoGameSolver()
        self.assertEqual(sln.get_secret_word(sample_case_0), "MOUSE")
        self.assertEqual(sln.get_secret_word(sample_case_1), "NOSE")
        self.assertEqual(sln.get_secret_word(sample_case_2), "GELATO")
