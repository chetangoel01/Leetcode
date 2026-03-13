class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boxstart = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]

        # check boxes
        for i in boxstart:
            r, c = i[0], i[1]
            numsset = set()
            for i in range(3):
                for j in range(3):
                    nextbox = (r+i, c+j)
                    if board[nextbox[0]][nextbox[1]].isdigit():
                        if board[nextbox[0]][nextbox[1]] not in numsset:
                            numsset.add(board[nextbox[0]][nextbox[1]])
                        else:
                            return False
        # check rows
        for i in range(9):
            numsset = set()
            for j in range(9):
                num = board[i][j]
                if num.isdigit():
                    if num not in numsset:
                        numsset.add(num)
                    else:
                        return False

        # check columns
        for j in range(9):
            numsset = set()
            for i in range(9):
                num = board[i][j]
                if num.isdigit():
                    if num not in numsset:
                        numsset.add(num)
                    else:
                        return False

        return True