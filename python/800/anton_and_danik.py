import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    s = input().strip()
    anton = []
    for i in s:
        if i in "A":
            anton.append(i)
    if len(anton) > n / 2:
        print("Anton")
    elif len(anton) == n/2:
        print("Friendship")
    else:
        print("Danik")


if __name__ == "__main__":
    solve()