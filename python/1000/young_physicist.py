import sys

input = sys.stdin.readline


def solve():
    n = int(input())
    X = []
    Y = []
    Z = []
    
    for _ in range(n):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
        all_x = sum(X)
        all_y = sum(Y)
        all_z = sum(Z)

    if all_x == all_y == all_z == 0:
        print("YES")
    else:
        print("NO")
        
    
if __name__ == "__main__":
    solve()