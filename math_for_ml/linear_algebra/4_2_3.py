import sys

import numpy as np


def main():
    import_data = sys.stdin.read().splitlines()
    matrix = np.array([np.fromstring(line, sep=" ", dtype=int) for line in import_data[:2]])
    target = np.fromstring(import_data[2], sep=" ", dtype=int)
    for w1 in range(-10, 11):
        for w2 in range(-10, 11):
            w = np.array([w1, w2])
            predict = matrix.T @ w.reshape(-1, 1)
            if (predict == target.reshape(-1, 1)).all():
                print(*w)
                return

    print("NO_SOLUTION")


if __name__ == "__main__":
    main()
