class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Approach : Take a Intersection and print the min value
        """intersection_set = set(nums1).intersection(set(nums2))
        if not intersection_set:
            return -1  
        return min(intersection_set) """

         # Approach 2 : Comapre and check 
        i = 0
        j = 0

        while i < len(nums1) and j < len(nums2):
            if  nums1 [i] == nums2[j]:
                return nums1[i]
            elif nums1[i]>nums2[j] : 
                j+=1
            else :
                i+=1
        return -1


        