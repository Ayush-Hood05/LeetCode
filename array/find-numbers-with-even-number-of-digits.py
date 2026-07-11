class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        """even_count = 0
        for i in range (0,len(nums)):
            num = nums[i]
            digit = 0
            while num > 0:
                num = num // 10
                digit += 1

            if digit % 2 == 0:
                even_count += 1
        return even_count """

        count = 0
        for i in nums :
            s = str(i)
            if len(s) % 2 == 0:
                count += 1

        return count



        