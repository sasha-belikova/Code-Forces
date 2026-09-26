import sys
input = sys.stdin.readline

def solve():
    a, b = input().split()
    a = int(a)  # Limak
    b = int(b)  # Bob (older)
    result = 0
    while a <= b:   # till Limak is smaller or equal to Bob
        a = a * 3
        b = b * 2
        result += 1
    print(result)     

if __name__ == "__main__":
    solve()