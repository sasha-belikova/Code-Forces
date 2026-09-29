import sys

input = sys.stdin.readline


def solve():
    n, k = input().split()
    n = int(n)   # whole number
    k = int(k)   # how many time we want to substract 1
    for _ in range(k):
        if n % 10 != 0:
            n = n - 1
        else:
            n = n // 10
    print(n)
    
if __name__ == "__main__":
    solve()