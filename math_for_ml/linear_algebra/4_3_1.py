import sys

import numpy as np


def main():
    input_data = sys.stdin.read().splitlines()
    matrix = np.array([np.fromstring(line, sep=" ", dtype=int) for line in input_data[1:]])
    umatrix = np.triu(matrix)
    lmatrix = np.tril(matrix)
    if np.array_equal(matrix, umatrix) and np.array_equal(matrix, lmatrix):
        print("DIAGONAL")
    elif np.array_equal(matrix, umatrix):
        print("UPPER_TRIANGULAR")
    elif np.array_equal(matrix, lmatrix):
        print("LOWER_TRIANGULAR")
    else:
        print("OTHER")


if __name__ == "__main__":
    main()
