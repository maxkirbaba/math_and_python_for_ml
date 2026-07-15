import sys

import numpy as np


def main():
    input_data = sys.stdin.read().splitlines()
    v = np.fromstring(input_data[1], sep=" ", dtype=int)
    u = np.fromstring(input_data[2], sep=" ", dtype=int)

    scalar_dot = v @ u
    norm_v = np.sqrt(v @ v)
    norm_u = np.sqrt(u @ u)

    cos = scalar_dot / (norm_u * norm_v)
    print(int(np.degrees(np.arccos(cos))))


if __name__ == "__main__":
    main()
