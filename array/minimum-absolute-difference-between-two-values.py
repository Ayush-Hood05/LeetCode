class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        ones = -1
        twos = -1
        min_abs = float('inf')

        for i in range (len(nums)):
            if nums[i] == 1:
                ones = i
                if twos != -1:
                    min_abs = min(min_abs,abs(ones-twos))
            elif nums[i] == 2:
                twos = i
                if ones != -1:
                    min_abs = min(min_abs,abs(ones-twos))

        if min_abs != float('inf'):
            return min_abs
        return -1