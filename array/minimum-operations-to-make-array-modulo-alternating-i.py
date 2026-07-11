class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # Cost of Remainder 
        even_cost = [0] * k  # [0,1,2]
        odd_cost = [0] * k

        # Calc for cost 
        for i in range(n):
            curr_rem = nums[i] % k
            for rem in range(k):
                diff = abs(curr_rem - rem)
                cost = min(diff , k-diff)

                if i % 2 == 0:
                    even_cost[rem] += cost
                else:
                    odd_cost[rem] += cost 

        min_ops = float('inf')

        # min cost finding
        for x in range(k):
            for y in range (k):
                if x != y:
                    curr_ops = even_cost[x] + odd_cost[y]
                    if curr_ops < min_ops:
                        min_ops = curr_ops
        return min_ops
                    