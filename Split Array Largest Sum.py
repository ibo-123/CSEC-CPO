class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def  can(max_sum):
            part = 1
            cur = 0
            for i in nums:
                if cur + i > max_sum:
                    part+=1
                    cur = i
                    if part > k:
                        return False
                else:
                    cur+=i
            return True
        left , right = max(nums) , sum(nums)
        while left < right:
            mid = (left + right)//2
            if can(mid):
                right = mid
            else:
                left = mid + 1
        return left
                    
