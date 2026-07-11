class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # dual looping 
        wealth = float('-inf')

        for i in range (0,len(accounts)):
            count = 0 
            for j in range (0,len(accounts[i])):
                count += accounts[i][j]
            
            wealth = max(count,wealth)

        return wealth
