class Solution:
    def removeOnes(self, grid):
        def flip(row):
            return [not i for i in row]
        
        pattern = grid[0]
        for i in range(1,len(grid)):
            if grid[i] == pattern or flip(grid[i]) == pattern:
                continue
            else:
                return False
        return True
