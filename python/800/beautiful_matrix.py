import sys
# import numpy as np

input = sys.stdin.readline

def solve():
    m = [list(map(int, input().split())) for i in range(5)]
    for i in range(5):
        for j in range(5):
            if m[i][j] == 1:
                n = abs(2 - i) + abs(2 - j)
    print(n)


# My first solution, using numpy but it had a RuntimeError

# def solve():
#     m = [list(map(int, input().split())) for i in range(5)]
#     matrix = np.array(m)
#     position = np.argwhere(matrix == 1)
#     numbers =  position[0]
#     i = numbers[0]
#     j = numbers[1]
#     if i != 2:
#         n = abs(2 - i)
#         if j != 2:
#             n += abs(2 - j)
#     else:
#         if j != 2:
#             n = abs(2 - j)
#     print(n)


    

if __name__ == "__main__":
    solve()