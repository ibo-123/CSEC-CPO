class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def check(mid):
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                return True
            else:
                return False
        def find():
            left , right = 0 , len(matrix) - 1
            while left <= right:
                mid = (left + right )//2
                if check(mid):
                    return matrix[mid]
                elif matrix[mid][-1] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return 0
        if find() == 0:
            print(find())
            return False
        l , r = 0 , len(matrix[0]) - 1
        m = find()
        while l <= r:
            mid = (l + r ) //2
            if m[mid] == target:
                return True
            elif m[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        print(0)
        return False
