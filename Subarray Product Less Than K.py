class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l , r = 0 , 0
        coun = 0
        mul = 1
        if k <= 1:
            return 0
        while r < len(nums):
            mul*=nums[r]
            while mul>=k and l < len(nums):
                mul//=nums[l]
                l+=1
                
            coun += r - l + 1
            r+=1
        return coun
