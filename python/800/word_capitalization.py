import sys
input = sys.stdin.readline

def solve():
    s = input().strip()
    result = s[0].upper() + s[1:]
    print(result)

if __name__ == "__main__":
    solve()