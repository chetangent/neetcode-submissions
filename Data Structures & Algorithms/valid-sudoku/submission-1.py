class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            r, c, b = set(), set(), set()
            for j in range(9):
                rv=board[i][j]
                if rv !=".":
                    if rv in r:
                        return False
                    r.add(rv)
                cv=board[j][i]
                if cv !=".":
                    if cv in c:
                        return False
                    c.add(cv)
                br=3*(i//3)+j%3
                bc=3*(i%3)+j//3
                bv=board[br][bc]
                if bv !=".":
                    if bv in b:
                        return False
                    b.add(bv)
        return True
