import sys

import numpy as np


def main():
    k = int(input())
    kef = np.array(list(map(float, input().split())))
    rows = []
    for _ in range(k):
        rows.append(list(map(float, input().split())))

    matrix = np.array(rows)
    ans1 = matrix * kef.reshape(-1, 1)
    print(*np.sum(ans1, axis=0).round(2))


if __name__ == "__main__":
    main()
