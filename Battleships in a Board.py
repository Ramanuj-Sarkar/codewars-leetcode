'''
You have an m by n matrix and there are battleships on it.
The battleships can be placed horizontally or vertically.

They are all either a single horizontal or vertical line,
1 x k (1 row, k columns) or k x 1 (k rows, 1 column)
where k can be any size.

There are also no adjacent battleships.
The board has at least one square, but that square can be empty.
'''
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        answer = 0
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    # all battleships have only one square
                    # for which neither of these holds
                    # because the battelships are all linear
                    if i > 0 and board[i-1][j] == 'X':
                        continue
                    if j > 0 and board[i][j-1] == 'X':
                        continue
                    answer += 1
        
        return answer
