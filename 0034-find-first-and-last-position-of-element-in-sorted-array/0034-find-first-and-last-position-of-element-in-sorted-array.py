class Solution(object):
    def searchRange(self, nums, target):
        ans = [-1,-1]
        start = self.search(nums,target,True)
        end = self.search (nums,target,False)
        ans[0] , ans[1] = start , end
        return ans 
    
    def search(self,nums,target,findStartIndex):
        start = 0
        end = len(nums) - 1
        ans = -1
        while start <= end : 
            mid = start + (end-start) // 2

            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else : 
                ans = mid 
                if findStartIndex == True :
                    end = mid - 1
                else : 
                    start = mid + 1
        return ans
