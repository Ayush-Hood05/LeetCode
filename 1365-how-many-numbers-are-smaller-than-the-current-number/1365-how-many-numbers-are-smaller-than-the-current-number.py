class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        greater = []
        n = len(nums)
        for i in range (n):
            count = 0
            for j in range (n):
                if nums[i] > nums[j]:
                    count += 1

            greater.append(count)

        return greater