class UniqueChar:

    @staticmethod
    def get_unique_chars(string):
        """
        remove duplicate char from string, not using additional memory (i.e use fixed buffer)
        :return unique characters from a string
        """
        seen_chars = [False] * 256
        for ch in string:
            if not seen_chars[ord(ch)]:
                seen_chars[ord(ch)] = True

        output = []
        for i in range(len(seen_chars)):
            if seen_chars[i]:
                output.append(chr(i))

        return output


print(UniqueChar.get_unique_chars("abcd"))  # expected: abcd
print(UniqueChar.get_unique_chars(""))  # expected: []
print(UniqueChar.get_unique_chars("a"))  # expected: []
print(UniqueChar.get_unique_chars("aaabbb"))  # expected: ab
