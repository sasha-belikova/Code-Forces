import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        x = 1
        n, k = input().split()
        n = int(n)  # сколько работает банк
        k = int(k)  # сколько раз он хочет снять денег
        if k == n:
            x = 2 * n
            print(x)
        else:
            rest = n - k
            x = 2 * (k - 1) + 2**(rest + 1)
            print(x)      

            

if __name__ == "__main__":
    solve()