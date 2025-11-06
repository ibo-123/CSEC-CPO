class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        max_length = 0
        coun = 0
        zeros = 0
        while right < len(nums):
            while zeros < 2 and right < len(nums):
                if nums[right] == 0:
                    zeros+=1
                if zeros < 2:
                    coun+=1
                right+=1
            if max_length < coun - 1:
                max_length = coun -1 
            while zeros == 2 and left < right:
                if nums[left] == 0:
                    zeros-=1
                    coun+=1
                coun-=1
                left+=1
            
        return max_length
