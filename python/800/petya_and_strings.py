import sys

input = sys.stdin.readline

def solve():
    a = str(input())
    b = str(input())
    a_lower = a.lower()
    b_lower = b.lower()
    if a_lower == b_lower:
        print(0)
    elif a_lower < b_lower:
        print(-1)
    else:
        print(1)



if __name__ == "__main__":
    solve()