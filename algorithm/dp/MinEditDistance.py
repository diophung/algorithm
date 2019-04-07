def min_edit(a, b, m, n):
    """
    return minimum number of insert/add/replace
    to make string a become string b
    """
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            # if first string is empty, the only solutiion
            # is to insert all characters of second string
            if i == 0:
                dp[i][j] = j

            # if second string is empty, the only solution
            # is to remove all characters of first string
            elif j == 0:
                dp[i][j] = i

            # if last character of two strings is the same
            # ignore last char and count for the remaining
            elif a[i - 1] == b[j - 1]:
                dp[i][j] == dp[i - 1][j - 1]
            # if last char is different, consider all possibilities
            # and find the minimum out of all
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],  # insert
                                   dp[i - 1][j],  # remove
                                   dp[i - 1][j - 1])  # replace

    pprint(dp)
    return dp[m][n]


def pprint(lst):
    for i in lst:
        print(i)


def editDistDP(str1, str2, m, n):
    # Create a table to store results of subproblems
    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Fill d[][] in bottom up manner
    for i in range(m + 1):
        for j in range(n + 1):

            # If first string is empty, only option is to
            # isnert all characters of second string
            if i == 0:
                dp[i][j] = j    # Min. operations = j

            # If second string is empty, only option is to
            # remove all characters of second string
            elif j == 0:
                dp[i][j] = i    # Min. operations = i

            # If last characters are same, ignore last char
            # and recur for remaining string
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            # If last character are different, consider all
            # possibilities and find minimum
            else:
                dp[i][j] = 1 + min(dp[i][j - 1],        # Insert
                                   dp[i - 1][j],        # Remove
                                   dp[i - 1][j - 1])    # Replace

    pprint(dp)
    return dp[m][n]


a = "these"
b = "thsee"
print(editDistDP(a, b, len(a), len(b)))
print(min_edit(a, b, len(a), len(b)))
