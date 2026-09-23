import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    a = [input().strip() for k in range(n)]
    x = 0
    for operation in a:
        if operation in "++X X++":
            x = x + 1
        else:
            x = x - 1
    print(x)

if __name__ == "__main__":
    solve()
