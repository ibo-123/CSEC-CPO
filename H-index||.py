class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def valid(h):
            left = 0
            right = len(citations) - 1
            while left <= right:
                mid = (left + right)//2
                if citations[mid] >= h :
                    right  = mid - 1
                else:
                    left = mid + 1
            return len(citations) - left >= h
            
        index = 0
        max_ = 0
        left , right = 0 , len(citations)-1
        while left <= right:
            mid = (right + left)//2
            print(mid , valid(mid + 1))
            if valid(mid + 1):
                left = mid + 1
                max_ = max(max_ , mid + 1)
            else:
                right = mid - 1
        if citations[0] >= len(citations):
            return len(citations) 
        return max_
