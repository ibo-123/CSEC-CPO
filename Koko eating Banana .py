class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        def can_eat(k):
            num = 0
            for i in piles:
                num = num +(i + k - 1 )//k
            if num <= h:
                    return True
            return False
        while left < right :
            mid = (left + right)//2
            if can_eat(mid):
                right = mid 
            else:
                left = mid + 1
        return left
