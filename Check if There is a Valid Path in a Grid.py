'''
You are given an m x n grid.

Each cell of grid represents a street.

The street of grid[i][j] can be:

    1 which means a street connecting the left cell and the right cell.
    2 which means a street connecting the upper cell and the lower cell.
    3 which means a street connecting the left cell and the lower cell.
    4 which means a street connecting the right cell and the lower cell.
    5 which means a street connecting the left cell and the upper cell.
    6 which means a street connecting the right cell and the upper cell.

'''
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        # we have already reached the end
        if m == n == 1:
            return True

        # the directions
        up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)

        # where you can go afterwards
        where_go = {1: {left, right},
        2: {up, down},
        3: {left, down},
        4: {right, down},
        5: {left, up},
        6: {right, up}}

        # original two directions you can go
        for odr, odc in where_go[grid[0][0]]:
            row, col = 0, 0
            dr, dc = odr, odc
            while True:
                nr, nc = row + dr, col + dc

                # checks it's on the grid
                if not (0 <= nr < m and 0 <= nc < n):
                    break

                # "backwards" direction
                corr = (-dr, -dc)
                
                # this new cell doesn't connect to the old one
                if corr not in where_go[grid[nr][nc]]:
                    break
                
                # we have reached the end
                if nr == m - 1 and nc == n - 1:
                    return True
                
                # we have gone in a loop
                # the other one would just be the backwards
                # version of this
                if nr == nc == 0:
                    return False
                
                # go to the next place instead of backwards
                dir1, dir2 = where_go[grid[nr][nc]]
                dr, dc = dir1 if dir1 != corr else dir2
                row, col = nr, nc
            
        # we didn't reach the end    
        return False
