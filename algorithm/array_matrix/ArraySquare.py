    
    str1 = "2, 5, 3, 11"
    str2 = "19, 25, 4, 181"
def find_square(arr1, arr2):
    """
    given 2 strings str1, str2 containing integers, find items in str2 which is 
    the square of items in str1.
    """

    
    """

    Naive algo: convert strings to arrays, sorted 2 arrays, use 2 pointers to 
    scan both array. At each scan, check for condition (x = y*y).

    Time complexity: max(O(mlog(m)), O(nlog(n)))

    m = len of arr1
    n = len of arr2
    """
    res = []
    if not str1 or not str2:
        return res
    # time spent sorting
    src = sorted([int(i) for i in str1.split(", ")])  # O1 = O(mlog(m))
    targ = sorted([int(i) for i in str2.split(", ")])  # O2 = O(nlog(n))
    
    i, j = 0, 0
    m, n = len(src), len(targ)
    # time spent scanning: O3 = O(m + n)
    while i < m and j < n:
        if pow(src[i], 2) == targ[j]:
            res.append(src[i])
            # assume: no duplicates in both
            i += 1
            j += 1
        elif targ[j] < pow(src[i], 2):
            j += 1
        else:
            i += 1
    # overall algorithm complexity: max(O1, O2, O3)
    return res
    
    
    print(solve(str1, str2))



