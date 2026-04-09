# Using a 2D matrix, create another kind of matrix
# where a single cell can be updated
# or you can take the sum of a rectangle 
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # deep copy of original matrix
        self.matrix = [[col for col in row] for row in matrix]
        
        # you can't change the original matrix
        # so you change this matrix
        # the column values include all values to the left
        for row in self.matrix:
            for col in range(1,len(row)):
                row[col] += row[col-1]
    
    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        original = self.matrix[row][col]
        if col != 0:
            original -= self.matrix[row][col-1]
            
        diff = original - val
        
        for y in range(col, len(self.matrix[0])):
            self.matrix[row][y] -= diff

    
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        '''
        Takes the rectangle defined by (row1, col1) and (row2, col2)
        and calculates the sum of all the cells within
        row1 <= row2, col1 <= col2
        '''
        region_sum = 0

        # the stuff to the left of col1 should be
        # subtracted only if it exists
        if col1 != 0:
            for x in range(row1, row2+1):  # we have two of the four points
                region_sum += self.matrix[x][col2]
                region_sum -= self.matrix[x][col1-1]
        else:
            for x in range(row1, row2+1):  # we have two of the four points
                region_sum += self.matrix[x][col2]
        
        return region_sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
