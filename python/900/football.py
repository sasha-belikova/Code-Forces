import sys
input = sys.stdin.readline

def solve():
    n = input().strip()
    null_ = 0
    one = 0
    result = "NO"
    for i in n:
        if i in "1":
            one += 1
            null_ = 0
        elif i in "0":
            one = 0
            null_ += 1
        if null_ >= 7 or one >= 7:
            result = "YES"
            print(result)
            break
    if result != "YES":
        print(result)            


if __name__ == "__main__":
    solve()