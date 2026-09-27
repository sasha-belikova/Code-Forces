import sys
input = sys.stdin.readline

def solve():
    x = int(input())
    if x % 5 == 0:
        result = x // 5
        print(result)
    else:
        result = x // 5 + 1
        print(result)

if __name__ == "__main__":
    solve()