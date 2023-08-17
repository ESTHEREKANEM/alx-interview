def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise
    Matrix is edited in-place
    Args:
        matrix
    """
    for layer in range(len(matrix) // 2):
        first = layer
        last = len(matrix) - layer - 1
        for i in range(last - first):
            temp = matrix[first][first + i]
            matrix[first][first + i] = matrix[last - i][first]
            matrix[last - i][first] = matrix[last][last - i]
            matrix[last][last - i] = matrix[first + i][last]
            matrix[first + i][last] = temp


