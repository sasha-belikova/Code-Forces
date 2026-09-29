import sys

input = sys.stdin.readline


def solve():
    s = str(input().strip())
    s = s.upper()
    s_no_vowels = "".join([symb for symb in s if symb not in "A O Y E U I"])
    s_with_dot = ".".join(s_no_vowels)
    print("." + s_with_dot.lower())
    
if __name__ == "__main__":
    solve()