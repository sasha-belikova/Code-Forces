import sys
input = sys.stdin.readline

def solve():
    n = input().strip()
    count = []
    for i in n:
        if i in "47":
            count.append(i)
    if len(count)== 4 or len(count) == 7:
        print("YES")
    else:
        print("NO")   

if __name__ == "__main__":
    solve()