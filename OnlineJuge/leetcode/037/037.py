class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board = [list(i) for i in board]
        print board
        def check(x,y,board):
            r_set = list(board[x])
            c_set = [board[c][y] for c in range(9)]
            b_set = [board[x//3*3+c][y//3*3+r] for c in range(3) for r in range(3)]
            return set( r_set + c_set + b_set )# - set(['.'])

        def boardempty(board):
            return [[[c,r],list(set("123456789")-check(c,r,board))] for c in range(9) for r in range(9) if board[c][r] == '.']
        
        def reshape(board):
            empty = boardempty(board)
            #print empty
            print len(empty)
            for i in range(len(empty)):
                #print empty[i]
                if len(empty[i][1]) == 1:
                    print empty[i]
                    board[empty[i][0][0]][empty[i][0][1]] = empty[i][1][0]
                    #empty.pop(i)
            #print board
            return board
        
        def solve(board):
            for c in range(9):
                for r in range(9):
                    if board[c][r] == '.':
                        tmp = list(set("123456789")-check(c,r,board))
                        if len(tmp) == 0:
                            return False
                        else:
                            for tn in tmp:
                                boardsave = board
                                board[c][r] = tn
                                board = reshape(board)
                                board = solve(board)
                                if board:
                                    return board
                                else:
                                    board = boardsave
                        return False
            return board
            
        boardnew = solve(board)
        print boardnew
        print board


s = Solution()
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s.solveSudoku(board)
