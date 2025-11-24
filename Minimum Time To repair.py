class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        m = sorted(ranks)

        left , right = 1 , m[-1]*(cars **2)
        def ispossible(time):
            total = 0
            for i in ranks:
                total+= int((time//i)**0.5)
                if total >= cars:
                    return True
            return False
        while left < right:
            mid = (right + left)//2
            if ispossible(mid):
                right = mid
            else:
                left = mid + 1
        return left
