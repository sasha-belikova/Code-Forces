import sys

input = sys.stdin.readline

def solve():
    s = str(input().strip())
    s_numbers = "".join([symb for symb in s if symb != "+"])
    s_sort = sorted(list(s_numbers))
    result = '+'.join(s_sort)
    print(result)
    

if __name__ == "__main__":
    solve()