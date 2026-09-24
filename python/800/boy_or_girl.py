import sys

input = sys.stdin.readline

def solve():
    n = input()
    only_org_letr = []
    for letter in n:
        if letter not in only_org_letr:
            only_org_letr.append(letter)
    indiv_number = len(only_org_letr) - 1   # as we have '/n' symbole from imput
    if indiv_number % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


if __name__ == "__main__":
    solve()