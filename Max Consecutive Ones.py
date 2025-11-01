class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_ = 0
        left = 0
        right = 0
        coun = 0
        zeros = 0
        while right < len(nums):
            if nums[right] == 0:
                    zeros+=1
            if zeros > k:
                if coun > max_:
                    max_ = coun
                while zeros > k and left < len(nums):
                    if nums[left] == 0:
                        zeros-=1
                        left+=1
                        break
                    coun-=1
                    left+=1
                
            else:
                coun+=1
            right+=1
        if coun > max_:
            max_ = coun
        return max_
            
