class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        # Two pointer 
        left = 0
        right = len(nums) - 1
        swap = 0

        while left < right :
            while nums[left] != 0 and left < right :
            # move left 
                left +=1
        
            while nums[right] == 0 and left < right :
            # move right
                right -= 1
        
            if left < right:
                nums[left], nums[right] = nums[right], nums[left]
                swap += 1
                left += 1
                right -= 1

        return swap