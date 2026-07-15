import sys


def main():
    p, s1, f1, s2, f2 = map(float, input().split())
    test1, test2 = map(int, input().split())

    really_sick = p * s1**test1 * (1 - s1) ** (1 - test1) * s2**test2 * (1 - s2) ** (1 - test2)
    healthy = (1 - p) * f1**test1 * (1 - f1) ** (1 - test1) * f2**test2 * (1 - f2) ** (1 - test2)
    print(really_sick / (healthy + really_sick))


if __name__ == "__main__":
    main()
