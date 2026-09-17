import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = [input() for k in range(n)]
    for word in a:
        currentLength = len(word) - 1   #input adds /n to transfer the line, thats why currentLength must be len(i) - 1
        if currentLength < 11:
            print(word)
        else:
            first = word[0]
            last = word[-2]
            number = len(word) - 2
            print(first + str(number) + last)

if __name__ == "__main__":
    solve()

