import sys
import math

input = sys.stdin.readline

def solve():
    n, m, a = map(int, input().split())
    n_part = math.ceil(n / a)
    m_part = math.ceil(m / a)
    print(n_part * m_part)


if __name__ == "__main__":
    solve()    