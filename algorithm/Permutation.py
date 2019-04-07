# Problem: given a string, find all permutation of this string
# permute("abc") -> abc, acb, bac, bca, cab, cba


def permute(s):
    output = []
    if len(s) == 1:
        return s
    for i in range(len(s)):
        remaining = s[:i] + s[i + 1:]
        for p in permute(remaining):
            output.append(s[i] + p)
    return set(output)


print(permute("abc"))
print(permute("1234"))
print(permute("0000"))
print(permute(["a", "permutation", "generator"]))
