class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def can(x):
            total = 0
            for i in candies:
                total+=i//x
            if total >= k:
                return True
            else:
                return False
        l , r = 1 , max(candies)
        ans = 0
        while l <= r:
            mid = (l+r)//2
            if can(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans
            
