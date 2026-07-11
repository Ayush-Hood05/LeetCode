class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.BinarySearch(nums, target, True)
        end = self.BinarySearch(nums, target, False)

        return [start, end]  

    def BinarySearch(self , nums , target , findfirstIndex):
        start = 0
        end = len(nums) - 1
        ans = -1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] > target:
                end = mid - 1

            elif nums[mid] < target:
                start = mid + 1

            else:
                ans = mid
                # Search of starting index 
                if findfirstIndex:
                    end = mid - 1
                # Searching for the end of index
                else:
                    start = mid + 1

        return ans