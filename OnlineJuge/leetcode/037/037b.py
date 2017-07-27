import copy
class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        boardnew = [list(i) for i in board]
        #print board
        def check(x,y,b):
            r_set = list(b[x])
            c_set = [b[c][y] for c in range(9)]
            b_set = [b[x//3*3+c][y//3*3+r] for c in range(3) for r in range(3)]
            return set( r_set + c_set + b_set )# - set(['.'])

        def boardempty(b):
            return [[[c,r],list(set("123456789")-check(c,r,b))] for c in range(9) for r in range(9) if b[c][r] == '.']
        
        def reshape(bnew):
            b = copy.deepcopy(bnew)
            empty = boardempty(b)
            f = False
            print empty
            print len(empty)
            for i in range(len(empty)):
                #print empty[i]
                if len(empty[i][1]) == 0:
                    return False,f
                if len(empty[i][1]) == 1:
                    f = True
                    b[empty[i][0][0]][empty[i][0][1]] = empty[i][1][0]
                    #empty.pop(i)
            #print board
            return copy.deepcopy(b),f
        
        def solve(b):
            for c in range(9):
                for r in range(9):
                    #r_b = reshape(b)
                    #if not r_b:
                        #return False
                    #else:
                        #b = r_b
                    if b[c][r] == '.':
                        #asave = copy.deepcopy(b)
                        #b = reshape(b)
                        #if not b:
                            #b = copy.deepcopy(asave)
                            #return False
                        tmp = list(set("123456789")-check(c,r,b))
                        #print tmp
                        for tn in tmp:
                            bsave = copy.deepcopy(b)
                            bsave[c][r] = tn
                            #b[c][r] = tn
                            #bsave = reshape(bsave)
                            #if not bsave:return False
                            tmp = solve(bsave)
                            if tmp:
                                b = copy.deepcopy(tmp)
                                return b
                            else:pass
                                #b = [i for i in bsave]
                                #b[c][r] = '.'
                        #b = copy.deepcopy(asave)
                        return False
            return b

        Flag = False
        while not Flag:
            boardnew, Flag = reshape(boardnew)
        a = solve(boardnew)
        board = [''.join(i) for i in a]
        print boardnew
        print board


s = Solution()
board = ["..9748...","7........",".2.1.9...","..7...24.",".64.1.59.",".98...3..","...8.3.2.","........6","...2759.."]
s.solveSudoku(board)
