import sys

input = sys.stdin.readline

def solve():
    n = int(input())
    a = [input() for k in range(n)]
    solved = []
    for task in a:
        together = int(task[0]) + int(task[2]) + int(task[4])             # I take 0, 2 and 4 to awoid spaces between numbers
        if together >= 2:
            solved.append(task)
    print(int(len(solved)))

if __name__ == "__main__":
    solve()