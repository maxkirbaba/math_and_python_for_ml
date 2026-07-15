import sys

import numpy as np


def main():
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return

    vector_u = np.fromstring(
        input_data[1], sep=" ", dtype=int
    )  # работает быстрее чем np.array(list(map(int, input_data[1].split())

    vector_v = np.fromstring(input_data[2], sep=" ", dtype=int)
    scalar_dot = vector_u @ vector_v  # .reshape() не нужен так как @ может вычислять и для одномерных векторов

    if scalar_dot == 0:
        print("ORTHOGONAL")
    else:
        print("NON-ORTHOGONAL")


if __name__ == "__main__":
    main()
