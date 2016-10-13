class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if len(board) <> 9 or len(board[0]) <> 9:return false
        
        def testSudoku(boardlist):
            itemmap = set()
            for item in boardlist:
                if item == '.':continue
                if item in itemmap:
                    return False
                else:itemmap.add(item)
            return True
        
        for column in board:
            if not testSudoku(column):return False
        for i in range(9):
            row = [r[i] for r in board]
            if not testSudoku(row):return False
        for i in range(0,9,3):
            for j in range(0,9,3):
                block = [board[i+x][j+y] for x in range(3) for y in range(3)]
                if not testSudoku(block):return False
                
        return True
