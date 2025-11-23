from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_arr = [[0] * cols for _ in range(rows)]

        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
               if col>0 and row>0:
                       self.prefix_arr[row][col]=matrix[row][col]+self.prefix_arr[row-1][col]+self.prefix_arr[row][col-1]-self.prefix_arr[row-1][col-1]
               elif col>0 and row<=0:
                       self.prefix_arr[row][col]=matrix[row][col]+self.prefix_arr[row][col-1]
               elif row>0 and col<=0:
                        self.prefix_arr[row][col]=matrix[row][col]+self.prefix_arr[row-1][col]
               else:
                        self.prefix_arr[row][col]=matrix[row][col]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total=self.prefix_arr[row2][col2]  
        if row1>0:
            total-=self.prefix_arr[row1-1][col2]        
        if col1>0:
            total-=self.prefix_arr[row2][col1-1]
        if row1>0 and col1>0:
            total+=self.prefix_arr[row1-1][col1-1]
        return total

