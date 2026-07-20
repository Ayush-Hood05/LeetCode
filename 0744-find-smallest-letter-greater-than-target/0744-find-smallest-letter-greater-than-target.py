class Solution(object):
    def nextGreatestLetter(self, letters, target):
        # Ceiling Problem 
        N = len(letters)
        start = 0
        end = len(letters)-1

        while start <= end : 
            mid = start + (end - start) // 2
            
            if letters[mid] > target:
                end = mid - 1
            else : 
                start = mid + 1
        
        # Lexicographically wrap around 
        return letters[start % N]
        