class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        row = rows//2
        column = len(matrix[row])
        col = column//2
        left = 0
        current = col * rows + row 
        right = column*rows-1
        while left <= right:
            current = (left+right)//2
            row = current//column
            col = current%column
            mid = matrix[row][col]
            if mid < target:
                left = current+1
                
            elif mid > target:
                right = current -1 
            else:
                return True
        return False