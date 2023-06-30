def multiply(mat1, mat2):
    m, k = len(mat1), len(mat1[0])
    n = len(mat2[0])
    
    # Initialize the result matrix with zeros
    result = [[0] * n for _ in range(m)]
    
    # Perform matrix multiplication
    for i in range(m):
        for j in range(n):
            for p in range(k):
                result[i][j] += mat1[i][p] * mat2[p][j]
    
    return result

# Test case
mat1 = [[1, 0, 0], [-1, 0, 3]]
mat2 = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
result = multiply(mat1, mat2)
print(result)
