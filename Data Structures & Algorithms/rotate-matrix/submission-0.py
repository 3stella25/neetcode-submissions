class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #rotate the matrix- move right, down, left, up. Traverse from left to right, up down. swap w/out saving
        #flip horizontally
        #flip diagonally
        #swap diagonally
        n = len(matrix)

        for row in range(n):
            for col in range(row + 1, n):
                matrix[row][col], matrix[col][row]  = matrix[col][row], matrix[row][col]
        #swap horizontally, 
        
        for row in range(n):
            for col in range(n // 2):
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]

        

        