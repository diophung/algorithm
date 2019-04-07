def longest_unique_substring(input):
    """Find the longest substring without repeating character"""
    start = max_len = 0
    used_char = {}

    # use a set to check of duplicate char
    for i in range(len(input)):
        # if not unique char
        if input[i] in used_char and start <= used_char[input[i]]:
            start = used_char[input[i]] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used_char[input[i]] = i
    return max_len


"""
aa -> 1


aab -> 2
aba -> 2

acee -> 3


"""