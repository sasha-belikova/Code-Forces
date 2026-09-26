import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        x = 0
        n, c = input().split()
        n = int(n)
        s = str(input().strip())
        half = n // 2
        for i in range(half):
            if s[i] == s[n-i-1]:
                x = x + 0
            elif s[i] == c or s[n-i-1] == c:
                x = x + 1 
            else:
                x = x + 2
        print(x)

            

if __name__ == "__main__":
    solve()
