import sys
input = sys.stdin.readline

def solve():
    k, n, w = map(int, input().split()) # k - first banana costs
                                        # n - amount of money that soldier has
                                        # w - how many bananas he want to buy
    price = 0
    for i in range(w+1):    # as we start with i = 0
        banana = k*i
        price += banana

    if price > n:           # check if soldier has enough money
        result = price - n
        print(result)
    else:
        print(0)

if __name__ == "__main__":
    solve()