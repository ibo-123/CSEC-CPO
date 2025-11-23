class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = 1
        for i in nums[1:]:
            nums[n]+=nums[n-1]
            n+=1
        return nums
