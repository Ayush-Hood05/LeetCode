class Solution:
    def compareBitonicSums(self, nums: list[int]) -> int:
        # find a peak
        n = len(nums)
        a_sum = 0
        d_sum = 0
        peak_idx = 0
        # Peak finder 
        for i in range (1,n):
            if nums[i] > nums[peak_idx]:
                peak_idx = i
        # Calucation 
        for i in range (0,peak_idx+1):
            a_sum +=nums[i]

        for j in range (peak_idx , n):
            d_sum +=nums[j]
        #case
        if a_sum > d_sum : 
            return 0
        elif d_sum > a_sum :
            return 1
        else : 
            return -1