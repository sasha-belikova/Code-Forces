import sys

input = sys.stdin.readline

def solve():
    m, n = map(int, input().split())
    cells = m * n 
    if cells >= 2:               # Check if a number is more or equal to 2
        if cells % 2 == 0:       # Check if a number is even           
            print(cells // 2)
        else:
            print((cells - 1) // 2)
    else:
        print(0)

if __name__ == "__main__":
    solve()