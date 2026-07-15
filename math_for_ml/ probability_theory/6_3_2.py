import sys


def main():
    m = int(input())
    count_A = 0
    count_B = 0
    count_C = 0
    count_ABC = 0
    count_AB = 0
    count_AC = 0
    count_BC = 0
    for _ in range(m):
        a, b, c = map(int, input().split())
        count_A += a
        count_B += b
        count_C += c
        if a == 1 and b == 1 and c == 1:
            count_ABC += 1
        if a == 1 and b == 1:
            count_AB += 1
        if a == 1 and c == 1:
            count_AC += 1
        if b == 1 and c == 1:
            count_BC += 1

    p_a = count_A / m
    p_b = count_B / m
    p_c = count_C / m
    p_ab = count_AB / m
    p_ac = count_AC / m
    p_bc = count_BC / m
    p_abc = count_ABC / m

    if (abs(p_ab - p_a * p_b) < 1e-9) and (abs(p_ac - p_a * p_c) < 1e-9) and (abs(p_bc - p_c * p_b) < 1e-9):
        if abs(p_abc - p_a * p_b * p_c) < 1e-9:
            print("ALL_INDEPENDENT")
        else:
            print("PAIRWISE_ONLY")
    else:
        print("NOT_INDEPENDENT")


if __name__ == "__main__":
    main()
