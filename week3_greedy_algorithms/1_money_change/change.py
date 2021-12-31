# Uses python3
import sys

def get_change(m):
    a = int(m / 10)
    b = int(m % 10 / 5)
    c = int(m % 10 % 5)
    return a+b+c

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
