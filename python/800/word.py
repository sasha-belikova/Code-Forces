import sys
input = sys.stdin.readline

def solve():
    s = str(input().strip())
    small = 0
    big = 0
    for i in s:
        if i == i.lower():    
            small += 1
        else:
            big += 1
    if small >= big:
        print(s.lower())
    else:
        print(s.upper())


if __name__ == "__main__":
    solve()