class Solution(object):
    def findMaxConsecutiveOnes(self, arr):
        max_one = 0
        count = 0
        for i in range (len(arr)):
            if arr[i] == 1 :
                count += 1
                if count > max_one:
                    max_one = count
            else : 
                    count = 0

        return max_one
        