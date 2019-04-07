# Problem : check if an array_matrix is a permutation of another array_matrix


def IsPermutation(array_a, array_b):
    count_a = {}
    count_b = {}
    for el in array_a:
        if count_a[el] is None:
            count_a[el] += 1
        count_a[el] = 1

    for el in array_b:
        if count_b[el] is None:
            count_b[el] += 1
        count_b[el] = 1

    for el in count_a:
        if count_b[el] != count_a[el]:
            return False
    return True


arr_a = ["a", "b", "c", "d"]
arr_b = ["b", "c", "d", "a"]
print(IsPermutation(arr_a, arr_b))
