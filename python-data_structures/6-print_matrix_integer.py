#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in len(matrix):
        for j in matrix[i]:
            if j == matrix[i][-1]:
                print(j)
            else:
                print("{:d}".format(j))
