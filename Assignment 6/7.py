def generateMatrix(n):
    # Initialize the matrix with zeros
    matrix = [[0] * n for _ in range(n)]
    
    # Define the boundaries of the matrix
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1
    
    num = 1  # Current number to fill in the matrix
    
    while num <= n * n:
        # Fill the top row from left to right
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Fill the right column from top to bottom
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        # Fill the bottom row from right to left
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = num
            num += 1
        bottom -= 1
        
        # Fill the left column from bottom to top
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = num
            num += 1
        left += 1
    
    return matrix

# Test case
n = 3
result = generateMatrix(n)
print(result)
