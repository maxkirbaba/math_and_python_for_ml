import itertools
import sys


def main():
    n, k = map(int, input().split())
    p = float(input())
    single_flip = [("орёл", p), ("решка", 1 - p)]
    ans = 0
    for seq in itertools.product(single_flip, repeat=n):
        curr_p = 1
        n_eagles = 0
        for flip in seq:
            curr_p = curr_p * flip[1]
            if flip[0] == "орёл":
                n_eagles += 1
        if n_eagles >= k:
            ans += curr_p
    print(ans)


if __name__ == "__main__":
    main()
