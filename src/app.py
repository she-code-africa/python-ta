import sys
import os


def fibonacci(n):
    r = list()

    for i in range(n):
        if i == 0 or i == 1:
            r.insert(i, i)
        else:
            v = r[i - 1] + r[i - 2]
            r.insert(i, v)

    return r


def solution(n):
    # Solution
    return fibonacci(n)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    n = int(sys.argv[1])
    print(solution(n))
