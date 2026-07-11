class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        # Main Situation : Customer can chosse min (m1,m2) , min > choosen candy 
        cost.sort() 
        n = len(cost)
        price = 0 
        ptr = n-1 

        while ptr > 1:
            price += cost[ptr]
            ptr -= 1
            price += cost[ptr]
            ptr -= 2
            
        # if len is 2 than by hole
        while ptr >= 0:
            price += cost[ptr]
            ptr -= 1

        return price


        

        

        

        