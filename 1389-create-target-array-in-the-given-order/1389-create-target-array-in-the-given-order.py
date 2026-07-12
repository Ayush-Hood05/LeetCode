class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        # We have to move the element right if they have the same index --> slide 
        for i in range(len(nums)):
            target.insert(index[i],nums[i])

        return target
