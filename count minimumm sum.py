class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        m = sorted(nums)
        right = 1
        left = 0
        coun = 0
        while left < len(m) -1:
            num_sum = m[right]+m[left]
            if num_sum < target:
                coun+=1
                if right < len(m) - 1:
                    right+=1
                else:
                    if left + 1 < len(m):
                        left+=1
                        right = left + 1
                    else:
                        break
            else:
                if len(m) > left + 1:
                    left+=1
                    right = left + 1
                else:
                    break
            
        return coun
