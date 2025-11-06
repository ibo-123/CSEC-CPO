class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        list_ = sorted(nums)
        left = 0
        right = len(nums)-1
        coun = 0
        while right > left:
            sum_ = list_[right] + list_[left]
            if sum_ == k:
                coun+=1
                right-=1
                left+=1
            elif sum_ > k:
                right-=1
            else:
                left+=1
        return coun
