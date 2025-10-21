class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = 0
        while len(nums1) > left  and len(nums2)> right:
            if nums1[left] == nums2[right] :
                return nums1[left]
            elif nums1[left] < nums2 [right] :
                left+=1
            else:
                right+=1 
        return -1
