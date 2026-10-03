class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        #iterate through the grid. Rows and columns
        #Compare as string value
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                 if self.exploreNum(row, col, grid, visited) == True:
                    num_islands += 1
        return num_islands

    def exploreNum(self, row, col, grid, visited):
        isValidRow = 0 <= row < len(grid)
        isValidCol = 0 <= col < len(grid[0])
        if not isValidRow or not isValidCol:
            return False
        position = str(row) + ',' + str(col)
        if position in visited:
            return False
        if grid[row][col] == '0':
            return False
        visited.add(position)
        self.exploreNum(row + 1, col, grid, visited)
        self.exploreNum(row - 1, col, grid, visited)
        self.exploreNum(row, col + 1, grid, visited)
        self.exploreNum(row, col - 1, grid, visited)
        return True