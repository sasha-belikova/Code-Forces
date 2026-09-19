import sys

input = sys.stdin.readline


def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    barrier = a[k - 1]
    next_round = []
    for point in a:       # Check the score of each participant
        if point > 0:     # The participant must have a score greater than 0
            if point >= barrier:        # The score must be at least as high as the k-th participant's score
                next_round.append(point)
    print(len(next_round))


if __name__ == "__main__":
    solve()