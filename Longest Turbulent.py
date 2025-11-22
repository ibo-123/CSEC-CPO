class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_ = 1
        index = 1

        up = down = 1
        while index < len(arr) :
            if arr[index] > arr[index-1]:
                up = down + 1
                down = 1
            elif arr[index] < arr[index - 1]:
                down = up + 1
                up = 1
            else:
                up = down = 1
            max_ = max(up , down , max_)
            index+=1
        return max_

            
