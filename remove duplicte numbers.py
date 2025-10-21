class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            if nums[i%len(nums)]==nums[(i-1)%len(nums)] and len(nums)>1:
                nums.pop(i%len(nums))
                continue
            i+=1
        return len(nums)       

