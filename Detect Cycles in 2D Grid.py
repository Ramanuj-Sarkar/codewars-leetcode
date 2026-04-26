'''
A cycle is a path of length 4 or more in the grid
that starts and ends at the same cell.

Given a 2D array of characters of size m x n,
which consists only of lowercase English letters
you need to find if there exists any cycle consisting of the same value.

From a given cell,
you can move to one of the cells adjacent to it
in one of the four directions (up, down, left, or right)
if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move.
For example, the cycle (1, 1) -> (1, 2) -> (1, 1) is invalid
because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists.
Otherwise, return false.
'''
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # seen cells
        seen = {}

        # the directions it can go
        directions = [(-1,0), (0,-1), (0,1), (1,0)]

        # checks if the cycle is valid
        # a single valid cycle is enough
        def valid_cycle(prev: tuple[int], curr: tuple[int], val):
            # add it to the seen cells
            seen[curr] = True
            
            for k in directions:
                # add curr and directions element-wise
                new_i, new_j = curr[0] + k[0], curr[1] + k[1]
                
                # check if either index is outside the grid
                if not (0 <= new_i < len(grid) and 0 <= new_j < len(grid[0])):
                    continue
                
                # checks if we're going back to the previous one
                # or the new value at this point is not the old value
                # either way, it wouldn't be a valid path
                # but that doesn't mean it's false yet
                if prev == (new_i, new_j) or grid[new_i][new_j] != val:
                    continue
                
                # if it ends in seen, the cycle is valid
                # it takes advantage of the fact that, as described
                # it is not possible for the cycle to have a length of 3 or less
                if (new_i, new_j) in seen or valid_cycle(curr, (new_i, new_j), val):
                    return True
            
            # no valid cycles were found
            return False

        # m x n
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if (i, j) in seen:
                    continue
                if valid_cycle((i, j), (i, j), grid[i][j]):
                    return True
        return False
