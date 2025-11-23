class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(weight):
            days_taken = 0
            weight_carry = 0
            for i in range(len(weights)):
                weight_carry += weights[i]
                if weight_carry > weight:
                    days_taken += 1
                    weight_carry = weights[i]
            
            if weight_carry > 0:
                days_taken += 1
            
            return days_taken <= days
        low, high = max(weights), sum(weights)
        answer = high
        while low <= high:
            mid = low + (high - low)//2
            if check(mid):
                answer = min(answer, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return answer
