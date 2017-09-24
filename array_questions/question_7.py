import math

# matrix coordinates
# lower_lim = 1; upper_lim = 2
# [
# [0,0 ; 0,1 ; 0,2 ; 0,3],
# [1,0 ; 1,1 ; 1,2 ; 1,3],
# [2,0 ; 2,1 ; 2,2 ; 2,3],
# [3,0 ; 3,1 ; 3,2 ; 3,3]
# ]


def get_edges (m, lower, upper):
    m_len = len(m[0])
    t_l = []
    t_r = []
    b_r = []
    b_l = []

    for j in range(lower, upper):
        t_l.append(m[lower][j])
        t_r.append(m[j][upper])

    for j in range(upper, lower, -1):
        b_r.append(m[upper][j])
        b_l.append(m[j][lower])

    return t_l, t_r, b_r, b_l


def rotate_matrix(m):
    upper_lim = len(m[0])
    iterations = math.ceil(upper_lim / 2)
    upper_lim -= 1
    lower_lim = 0

    while lower_lim < iterations:
        if (upper_lim - lower_lim) == 0:
            return m

        # swap
        t_r, b_r, b_l, t_l = get_edges(m, lower_lim, upper_lim)

        k = 0
        for j in range(lower_lim, upper_lim):
            m[lower_lim][j] = t_l[k]
            m[j][upper_lim] = t_r[k]
            k += 1

        k = 0
        for j in range (upper_lim, lower_lim, -1):
            m[upper_lim][j] = b_r[k]
            m[j][lower_lim] = b_l[k]
            k += 1

        upper_lim -= 1
        lower_lim += 1

    return m


def main():
    matrix1 = [
        [3, 4, 5],
        [7, 8, 9],
        [12, 13, 14]
    ]

    matrix_len = len(matrix1[0])
    rotated_matrix = rotate_matrix(matrix1)

    for i in range(matrix_len):
        print(rotated_matrix[i])

    matrix2 = [
        [3, 4, 5, 6],
        [7, 8, 9, 10],
        [12, 13, 14, 15],
        [20, 21, 22, 23]
    ]

    matrix_len = len(matrix2[0])
    rotated_matrix = rotate_matrix(matrix2)

    print()
    for i in range(matrix_len):
        print(rotated_matrix[i])


if __name__ == '__main__':
    main()
