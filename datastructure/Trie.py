from TrieNode import TrieNode
import unittest


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Insert new word into the trie
        """
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c] = TrieNode()
            curr_node = curr_node.children[c]
        curr_node.is_last = True

    class Trie:

        def __init__(self):
            self.root = TrieNode()

        def insert(self, word):
            """
            Insert new word into the trie
            """
            curr_node = self.root
            for c in word:
                if c not in curr_node.children:
                    curr_node.children[c] = TrieNode()
                curr_node = curr_node.children[c]
            curr_node.is_last = True

        def remove(self, node, word, depth):
            if not node:
                return None

            if depth == len(word):
                if node.is_last:
                    node.is_last = False
                if not node.children:
                    node = None
                return node

            ch = word[depth]
            node.children[ch] = self.remove(node.children[ch], word, depth + 1)
            # if node
            if not node.children and not node.is_last:
                node = None

            return node

        def search(self, word):
            """Return True if the whole word is in Trie"""
            curr_node = self.root
            for c in word:
                if c not in curr_node.children:
                    return False
                curr_node = curr_node.children[c]
            return curr_node.is_last  # go to the end, check if whole word fit the Trie

        def contains(self, prefix):
            """Return True if there are words starts with the prefix"""
            pointer = self.root
            for c in prefix:
                if c not in pointer.children:
                    return False
                pointer = pointer.children[c]
            return True  # go to the end, check if prefix is subset of Trie

        def get_matches(self, node, prefix, output):
            """ return all words in Trie that start with "prefix" """
            # this is a complete word
            if node.is_last:
                output.append(prefix)

            # branch out to collect words
            for key, child in node.children.items():
                self.get_matches(child, prefix + key, output)

        def get_autocompletion(self, prefix):
            """Find all words that start with this prefix"""
            curr_node = self.root
            # traverse the trie using prefix
            for ch in prefix:
                if ch not in curr_node.children:
                    return []
                curr_node = curr_node.children[ch]

            output = []
            self.get_matches(curr_node, prefix, output)
            return output

        def pprint(self, node):
            for k, v in node.children.items():
                print(k)
                self.pprint(v)

        def populate(self, words):
            for w in words:
                self.insert(w)

    def remove(self, node, word, depth):
        if not node:
            return None

        if depth == len(word):
            if node.is_last:
                node.is_last = False
            if not node.children:
                node = None
            return node

        ch = word[depth]
        node.children[ch] = self.remove(node.children[ch], word, depth + 1)
        # if node
        if not node.children and not node.is_last:
            node = None

        return node

    def search(self, word):
        """Return True if the whole word is in Trie"""
        curr_node = self.root
        for c in word:
            if c not in curr_node.children:
                return False
            curr_node = curr_node.children[c]
        return curr_node.is_last  # go to the end, check if whole word fit the Trie

    def contains(self, prefix):
        """Return True if there are words starts with the prefix"""
        pointer = self.root
        for c in prefix:
            if c not in pointer.children:
                return False
            pointer = pointer.children[c]
        return True  # go to the end, check if prefix is subset of Trie

    def get_matches(self, node, prefix, output):
        """ return all words in Trie that start with "prefix" """
        # this is a complete word
        if node.is_last:
            output.append(prefix)

        # branch out to collect words
        for key, child in node.children.items():
            self.get_matches(child, prefix + key, output)

    def get_autocompletion(self, prefix):
        """Find all words that start with this prefix"""
        curr_node = self.root
        # traverse the trie using prefix
        for ch in prefix:
            if ch not in curr_node.children:
                return []
            curr_node = curr_node.children[ch]

        output = []
        self.get_matches(curr_node, prefix, output)
        return output

    def pprint(self, node):
        for k, v in node.children.items():
            print(k)
            self.pprint(v)

    def populate(self, words):
        for w in words:
            self.insert(w)


class TrieUnitTest(unittest.TestCase):
    def test_positive_cases(self):
        trie = Trie()
        words = ["aaron", "aaron2", "about", "abab", "bat", "bacteria", "christ", "christmas"]
        trie.populate(words)

        self.assertTrue(trie.search("about"))  # True
        self.assertIsNone(trie.get_autocompletion("d"))  # None
        self.assertEqual(trie.get_autocompletion("aar"), ["aaron", "aaron2"])  # ["aaron", "aaron2"]
        self.assertEqual(trie.get_autocompletion("aaron2"), ["aaron2"])  # ["aaron2"]
        self.assertIsNone(trie.get_autocompletion("aaron23"))  # None
