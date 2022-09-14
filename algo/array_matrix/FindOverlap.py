# find intersection between intervals


def find_interval_overlap(first, second):
    if second[0] < first[0]:
        first, second = second, first
    
    # full encompassed
    if second[1] <= first[1]:
        return second[0], second[1]
    
    # partial overlap
    if second[0] <= first[1]:
        return second[0], first[1]
    
    # no overlap
    if first[1] < second[0]:
        return None


print(find_interval_overlap((0, 10), (1, 5)))  # --> [1, 5]
print(find_interval_overlap((1, 8), (7, 10)))  # --> [7, 8]
print(find_interval_overlap((1, 5), (6, 10)))  # --> []
