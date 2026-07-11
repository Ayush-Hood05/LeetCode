# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# Disclaimer : mountainArr is not a standard Python list. It is a custom object defined by the platform (like LeetCode), and it acts as an interface to protect the underlying data.

# for length use : .length() and to acess value use : .get()
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        peak = self.helper_peak(mountainArr, n)

        ascending = self.Binary_search(mountainArr, target, 0, peak, True)
        if ascending != -1:
            return ascending

        descending = self.Binary_search(mountainArr, target, peak, n - 1, False)
        return descending


    def helper_peak(self,mountainArr , n):
        start = 0
        end = n - 1  
        
        while start < end:

            mid = start + (end - start) // 2
            # Use the .get() API 
            if mountainArr.get(mid) > mountainArr.get(mid + 1):
                end = mid
            else:
                start = mid + 1
        return start

    def Binary_search(self,mountainArr,target,start,end,flag):
        while start <= end:
            mid = start + (end - start) // 2
            mid_val = mountainArr.get(mid)

            if mid_val == target:
                return mid
            
            if flag:
                if target > mid_val:
                    start = mid + 1
                else:
                    end = mid - 1
            else:

                if target < mid_val:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return -1
 