class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        def check(x,y):
            r_set = set(board[x])
            c_set = set([board[c][y] for c in range(9)])
            b_set = set([board[x//3*3+c][y//3*3+r] for c in range(3) for r in range(3)])
            return board[x][y] in ( r_set | c_set | b_set ) - set(['.'])
        
        pointlist = [[i,j,list(set(range(1,10)) - check([i,j]))] for i in range(9) for j in range(9)]


