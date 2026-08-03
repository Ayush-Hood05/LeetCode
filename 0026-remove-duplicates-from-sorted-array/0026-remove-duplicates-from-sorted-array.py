class Solution(object):
    def removeDuplicates(self, nums):
        n = len(nums) 
        idx = 1
        for j in range (1,n):
            if nums[idx-1] != nums[j]:
                nums [idx] = nums[j]
                idx += 1
        return idx 
