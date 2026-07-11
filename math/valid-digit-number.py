class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        # X should be there 
        # X should not start
        num = str(n) 
        if len(num) == 1:
            return False
        if num[0] == str(x) :
            return False 
        for i in range (1,len(num)):
            if num[i] == str(x):
                # one occurance 
                return True 
        return False