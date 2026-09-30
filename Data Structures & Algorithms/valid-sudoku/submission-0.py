class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = 0
        row = 0
        while col < 9:
            if not self.checkRow(board[col]):
                return False
            col+=1
        while row < 9:
            if not self.checkCol(board,row):
                return False 
            row +=1
        if not self.checkGrid(board,0):
            return False
        if not self.checkGrid(board,3):
            return False        
        if not self.checkGrid(board,6):
            return False
        if not self.checkGrid(board,27):
            return False
        if not self.checkGrid(board,30):
            return False
        if not self.checkGrid(board,33):
            return False
        if not self.checkGrid(board,54):
            return False
        if not self.checkGrid(board,57):
            return False
        if not self.checkGrid(board,60):
            return False
        return True


    def checkRow(self,row:List[str]) -> bool:
        seen = {}
        for char in row:
            if char=='.':
                continue
            if char not in seen:
                seen[char]=1
            else:
                return False
        return True

    def checkCol(self, board: List[List[str]],num:int) -> bool:
        col = 0
        collist={}
        while col < 9:
            if board[col][num]=='.':
                col+=1
                continue            
            if board[col][num] not in collist:
                collist[board[col][num]] =1
            else:
                return False
            col+=1
        return True

    
    def checkGrid(self, board: List[List[str]],index) -> bool:
        startrow = index%9
        startcolumn = index//9
        seen ={}
        for row in range(startrow,startrow+3):
            for column in range(startcolumn,startcolumn+3):
                if board[row][column] == '.':
                    continue
                if board[row][column] in seen:
                    return False
                else:
                    seen[board[row][column]] =1 
        return True
            


