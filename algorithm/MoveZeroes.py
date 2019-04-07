# LeetCode #283: Given an array_matrix nums, write a function to move all 0's to the end
# of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
# should be [1, 3, 12, 0, 0].

# Note:
# You must do this in-place without making a copy of the array_matrix.
# Minimize the total number of operations.


class MoveZeroes:
    def moveZeroes(self, nums):
        idx_of_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[i]
                nums[i] = nums[idx_of_zero]
                nums[idx_of_zero] = temp
                idx_of_zero += 1
        return nums


solver = MoveZeroes()
print(solver.moveZeroes([0, 2, 1, 0, 13, 12]))  # expect [1, 13, 12, 0, 0]
print(solver.moveZeroes([0, 0, 1]))  # expect [1, 0, 0]
print(solver.moveZeroes([0]))  # expect [0]
print(solver.moveZeroes([0, 0]))  # expect [0, 0]
print(solver.moveZeroes([1]))  # expect [1, 2]
