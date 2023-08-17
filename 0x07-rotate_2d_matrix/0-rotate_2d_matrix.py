def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix 90 degrees clockwise
    Matrix is edited in-place
    Args:
        matrix
    """
    left, right = 0, len(matrix) - 1

    while left < right:
        i = 0
        while i < right - left:
            top, bottom = left, right
            # save topleft  value
            topLeft = matrix[top][left + i]
            # move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # move top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # move top left to top right
            matrix[top + i][right] = topLeft
            i += 1
        right -= 1
        left += 1
