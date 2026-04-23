'''
A falling path starts at any element in the first row
and chooses the element in the next row that is
either directly below or diagonally left/right
(the three cells below the element which touch its corners).

Given an n x n array of integers matrix,
return the minimum sum of any falling path through matrix.
'''
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # a is copy which ensures original doesn't get used up
        a = [[c for c in r] for r in matrix]
        lm = len(matrix)
        
        for i in range(1,lm):
            for j in range(lm):
                # finds values of cells above
                # which touch the corners of that cell
                # directly above / to the left / to the right respectively
                a[i][j] += min([a[i - 1][j],
                a[i-1][max(0,j-1)],
                a[i-1][min(lm-1,j+1)]])
        
        # find the minimum value of the last row
        return min(a[lm-1])
