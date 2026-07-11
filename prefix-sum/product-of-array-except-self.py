class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix
        n =len(nums)
        prefix = [1]*n
        res = [1]*n
        for i in range(1,n):
            prefix[i] = nums[i-1] * prefix[i-1]
        # Suffix
        suffix = [1]*n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        for i in range (0,n):
            res[i] = prefix[i] * suffix[i]
        return res