class TrieNode:

    def __init__(self):
        self.children = {}  # assuming ASCII alphabet, case-insensitive
        self.is_last = False  # mark the end of a word

