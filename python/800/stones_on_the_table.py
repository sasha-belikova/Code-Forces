import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = str(input())
    result = 0
    for i in range(n - 1):
        current = s[i]
        next = s[i + 1]
        if current == next:
            result += 1
    print(result)
    

if __name__ == "__main__":
    solve()