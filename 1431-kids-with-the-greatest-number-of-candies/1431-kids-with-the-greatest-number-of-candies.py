class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        n = len(candies)
        flags = []
        for i in range (n):
            if candies[i] + extraCandies >= max_candies : 
                flags.append(True)
            else : 
                flags.append(False)

        return flags 
