class TextJustification:
    @staticmethod
    def justify(words: list, max_width: int) -> list:
        """
        PROBLEM: Text justification
        ------------
        Given an array_matrix of words and a length maxWidth, format the text
        such that each line has exactly maxWidth characters and is fully
        (left and right) justified. You should pack your words in
        a greedy approach; that is, pack as many words as you can
        in each line. Pad extra spaces ' ' when necessary so that
        each line has exactly maxWidth characters.

        Extra spaces between words should be distributed as evenly
        as possible. If the number of spaces on a line do not
        divide evenly between words, the empty slots on the left
        will be assigned more spaces than the slots on the right.

        For the last line of text, it should be left justified and
        no extra space is inserted between words.

        For example,
        words: ["This", "is", "an", "example", "of", "text", "justification."]
        maxWidth: 16.
        Return the formatted lines as:
        [
           "This    is    an",
           "example  of text",
           "justification.  "
        ]

        Args:
            words (list(str)): input as words
            max_width (int): max char on a line

        Returns:
            list(str): the justified strings with appended space
        """
        curr_line, output, char_count = [], [], 0
        for w in words:
            # need new line
            if char_count + len(w) + len(curr_line) > max_width:
                # put spaces between words with round-robin
                for i in range(max_width - char_count):
                    curr_line[i % (len(curr_line) - 1 or 1)] += ' '
                output.append(''.join(curr_line))
                curr_line, char_count = [], 0
            curr_line += [w]
            char_count += len(w)
        # last line
        return output + [' '.join(curr_line).ljust(max_width)]


words = ["This", "is", "an", "example", "of", "text", "justification."]
lines = TextJustification.justify(words, 16)
for l in lines:
    print(l)

"""
EXPECT:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""