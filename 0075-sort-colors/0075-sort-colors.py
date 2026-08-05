class Solution(object):
    def sortColors(self, nums):
        n = len(nums)
        # Selection Sort 
        for i in range (n):
            min_idx = i
            for j in range (i,n):
                if nums[min_idx] > nums [j]:
                    min_idx = j

            # swap 
            nums[min_idx] , nums [i] = nums[i] , nums[min_idx]
        