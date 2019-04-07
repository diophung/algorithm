# Prob: find the max size of the subarray (collection of continuous elements)
# which sums up to an integer k. If no subarray can be found, return 0

# Algo:
# Build a hashmap to store sum of all elements before index i-th as key, i-th as value.
# As we build the hashmap, if we detect there is an exact increasement of K, i.e prevSum (currentSum - K) exists
# in the map, then we've found such subarray which sum up to K. Get ans by find max between currentAns
# and index differences between currentSum (i) and prevSum (map[currentSum - K])


class MaxSubArray:
    @staticmethod
    def solve(nums: list, k: int) -> int:
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, tsum = 0, 0  # answer and the accumulative value of nums
        map_idx = {0: -1}  # key is tsum value, and value is the index
        for i in range(len(nums)):
            tsum += nums[i]
            if tsum not in map_idx:
                map_idx[tsum] = i
            if tsum - k in map_idx:
                ans = max(ans, i - map_idx[tsum - k])
        return ans


solver = MaxSubArray()
# expect 4 since sum [1, -1, 5, -2] = 3
solution = solver.solve([1, -1, 5, -2, 3], 3)
print(solution)

# expect 2 since sum [5, -2] = 3
solution = solver.solve([1, 11, 5, -2, 3], 3)
# map[value -> index]
# 1 -> 0 , tsum - k = 2, ans = 0
# 12 -> 1, tsum - k = 9, ans = 0
# 17 -> 2, tsum - k = 14, ans = 0
# 15 -> 3, tsum - k = 12, ans = max(0, 3 - map[12]=1) = 2
# 18 -> 4, tsum - k = 15, ans = max(2, 4 - map[15]=3) = 2
print(solution)
