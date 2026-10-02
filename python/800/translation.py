import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    t = input().strip()
    s = list(s)
    t = list(t)
    if list(reversed(s)) == t:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    solve()