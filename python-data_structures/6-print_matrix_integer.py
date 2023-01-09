#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print()
    else:
        for i in range(len(matrix)):
            for j in matrix[i]:
                if j == matrix[i][-1]:
                    print(j)
                else:
                    print("{:d}".format(j), end=" ")
