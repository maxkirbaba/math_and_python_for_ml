import sys


def main():
    c, d = map(float, input().split())
    if d <= 0:
        print(0)
    elif 0 < d <= c:
        print((d**2 / 2) / c**2)
    elif c < d < 2 * c:
        print((c**2 - ((2 * c - d) ** 2 / 2)) / c**2)
    elif d >= 2 * c:
        print(1)


if __name__ == "__main__":
    main()
