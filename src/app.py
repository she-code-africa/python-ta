import sys
import os


def prime(s):
    # your code goes here
    source = []
    for letter in s:
        letter = letter.strip()
        letter = letter.lower()
        if len(letter) <= 0:
            continue
        source.append(letter)
    account = (len(source) - 1)
    for entry in source:
        if entry == source[account]:
            account -= 1
            continue
    if account == -1:
        print(s)
def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
