# comments should explain everything
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # matrix rotation = diagonal flip + vertical flip
        n = len(matrix)
        for row in range(n):
            for col in range(row, n):
                # diagonal flip
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        
        
        for row in range(n):
            # vertical flip
            matrix[row] = list(reversed(matrix[row]))
