class Solution(object):
    def sortColors(self, nums):
        # this question has only 0,1,2 keys therefore 
        low = 0 # for 0's
        mid = 0 # for 1's
        high = len(nums) - 1 # for 2's

        while mid <= high : 
            if nums[mid] == 0:
                nums[low] , nums[mid] = nums[mid] , nums[low]
                mid += 1
                low += 1

            elif nums[mid] == 1:
                nums[mid] = 1
                mid += 1
        
            else : 
                nums[mid] , nums[high] = nums[high] , nums[mid]
                high -= 1
        