from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        new = defaultdict(int)
        new[0] = 1
        total = 0
        result = 0
        for num in nums:
            total+=num
            mod = total%k
            if mod < 0:
                mod+=k
            result +=new[mod]
            new[mod]+=1
        return result
