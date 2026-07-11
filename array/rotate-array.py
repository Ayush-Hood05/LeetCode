class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """n = len(nums)
        for i in range (k):
            last = nums[n-1]
            for j in range(n-2,-1,-1):
                nums[j+1] = nums[j]
            nums[0] = last"""
        n = len(nums)
        k %= n
        nums[:] = nums[n-k:] + nums[:n-k]
        """
        Do not return anything, modify nums in-place instead.
        """
        