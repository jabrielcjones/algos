
def rotate(matrix):
    """
    Do not return anything, modify matrix in-place instead.

    N x N 2D matrix representing an image

    Contraints:
        * matrix.length == n
        * matrix[i].length == n
        * 1 <= n <= 20
        * -1000 <= matrix[i][j] <= 1000

    """

    corners = _get_corners(matrix)    

    _print_image(matrix)

    matrix = _shift_edges(matrix, corners, False)

    _print_image(matrix)

def _get_corners(matrix):
    """
    """

    corners = {}

    corners['upper_left_index'] = [0, 0]
    corners['upper_right_index'] = [0, len(matrix)-1]

    corners['lower_left_index'] = [len(matrix)-1, 0]
    corners['lower_right_index'] = [len(matrix)-1, len(matrix)-1]

    return corners

def _update_corners(corners):
    """
    """

    for i in range(0, len(corners['upper_left_index'])):
        corners['upper_left_index'][i] += 1

    corners['upper_right_index'][0] += 1
    corners['upper_right_index'][1] -= 1

    corners['lower_left_index'][0] -= 1
    corners['lower_left_index'][1] += 1

    for i in range(0, len(corners['lower_right_index'])):
        corners['lower_right_index'][i] -= 1

def _get_edges(matrix, corners):
    """
    """

    edges = {}

    # Edge A - upper_left to upper_right
    edge_A = []
    start = corners['upper_left_index'][1]
    end = corners['upper_right_index'][1]

    row = corners['upper_left_index'][0]

    for i in range(start, end + 1):
        edge_A.append(matrix[row][i])

    edges['A'] = edge_A

    # Edge B - upper_left to upper_right
    edge_B = []
    start = corners['lower_right_index'][0]
    end = corners['upper_right_index'][0]

    column = corners['lower_right_index'][1]

    for i in range(start, end - 1, -1):
        edge_B.append(matrix[i][column])

    edges['B'] = edge_B

    # Edge C - lower_left to lower_right
    edge_C = []
    start = corners['lower_left_index'][1]
    end = corners['lower_right_index'][1]

    row = corners['lower_left_index'][0]

    for i in range(start, end + 1):
        edge_C.append(matrix[row][i])

    edges['C'] = edge_C

    # Edge D - lower_left to upper_right
    edge_D = []
    start = corners['lower_left_index'][0]
    end = corners['upper_left_index'][0]

    column = corners['lower_left_index'][1]

    for i in range(start, end - 1, -1):
        edge_D.append(matrix[i][column])

    edges['D'] = edge_D

    return edges

def _print_image(matrix):
    """
    """

    print('Image:')
    for row in matrix:
        print(row)

def _shift_edges(matrix, corners, terminal_flag):
    """
    """

    center = []
    center.append(int(len(matrix)/2))
    center.append(int(len(matrix)/2))

    if center == [0,0]:
        return matrix

    # Get edges using corners
    edges = _get_edges(matrix, corners)

    # Shift A to B
    start = corners['upper_right_index'][0]
    end = corners['lower_right_index'][0]

    column = corners['upper_right_index'][1]
    for row, item in zip(range(start, end + 1), edges['A']):
        matrix[row][column] = item

    # Shift B to C
    start = corners['lower_left_index'][1]
    end = corners['lower_right_index'][1]

    row = corners['lower_left_index'][0]

    for column, item in zip(range(start, end + 1), edges['B']):
        matrix[row][column] = item

    # Shift C to D
    start = corners['upper_left_index'][0]
    end = corners['lower_left_index'][0]

    column = corners['upper_left_index'][1]

    for row, item in zip(range(start, end + 1), edges['C']):
        matrix[row][column] = item

    # Shift D to A
    start = corners['upper_left_index'][1]
    end = corners['upper_right_index'][1]

    row = corners['upper_left_index'][0]

    for column, item in zip(range(start, end + 1), edges['D']):
        matrix[row][column] = item

    _update_corners(corners)

    odd_matrix = True
    if len(matrix) % 2 == 0:
        odd_matrix = False

    center = []
    center.append(int(len(matrix)/2))
    center.append(int(len(matrix)/2))

    if odd_matrix:
        for item in corners.values():
            if center == item:
                return matrix

    else:
        if terminal_flag:
            return matrix

        for item in corners.values():
            if center == item:
                terminal_flag = True

    return _shift_edges(matrix, corners, terminal_flag)

def main():
    # test 1
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(matrix)

    # test 2
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(matrix)

    # test 3
    matrix = [[1]]
    rotate(matrix)

    # test 4
    matrix = [[1,2],[3,4]]
    rotate(matrix)

if __name__ == "__main__":
    main()