class Solution(object):
    def moveZeroes(self, nums):
        n = len(nums)
        ptr = 0
        for i in range (n):
            if nums[i] != 0:
                nums[i] , nums[ptr] = nums[ptr] , nums[i]
                ptr += 1
        return nums
        

        
        