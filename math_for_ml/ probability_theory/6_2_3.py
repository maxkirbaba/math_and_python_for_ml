import sys


def main():
    r, g, b = map(int, input().split())
    s = r + g + b
    first = 1 - (((r + b) * (r + b - 1) * (r + b - 2)) / (s * (s - 1) * (s - 2)))
    second = (g * (g - 1) * (g - 2) + r * (r - 1) * (r - 2) + b * (b - 1) * (b - 2)) / (s * (s - 1) * (s - 2))
    print(first, second)


if __name__ == "__main__":
    main()
