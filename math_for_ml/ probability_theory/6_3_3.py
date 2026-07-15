import math
import sys


def main():
    m_train, n_test, k_words = map(int, input().split())
    train_data = []
    spam = 0
    not_spam = 0
    for i in range(m_train):
        row = list(map(int, input().split()))
        if row[0] == 1:
            spam += 1
        elif row[0] == 0:
            not_spam += 1
        train_data.append(row)

    p_spam = spam / m_train
    p_notspam = not_spam / m_train

    s = [0] * k_words
    ns = [0] * k_words
    for object in train_data:
        if object[0] == 0:
            for j in range(1, k_words + 1):
                if object[j] == 1:
                    ns[j - 1] += 1
        else:
            for i in range(1, k_words + 1):
                if object[i] == 1:
                    s[i - 1] += 1

    for i in range(k_words):
        s[i] = s[i] / spam
        ns[i] = ns[i] / not_spam

    ans = []
    for j in range(n_test):
        test_row = list(map(int, input().split()))
        test_spam = []
        test_not_spam = []
        for k in range(k_words):
            if test_row[k] == 0:
                test_spam.append(1 - s[k])
                test_not_spam.append(1 - ns[k])
            else:
                test_spam.append(s[k])
                test_not_spam.append(ns[k])

        p_test_not_spam = math.prod(test_not_spam) * p_notspam
        p_test_spam = math.prod(test_spam) * p_spam
        if p_test_spam > p_test_not_spam:
            ans.append(1)
        elif p_test_spam < p_test_not_spam:
            ans.append(0)
        elif abs(p_test_not_spam - p_test_spam) <= 1e-5:
            ans.append(-1)

    print(*ans, sep=" ")


if __name__ == "__main__":
    main()
