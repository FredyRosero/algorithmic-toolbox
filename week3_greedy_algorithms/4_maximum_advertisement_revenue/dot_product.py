#Uses python3

import sys

def max_dot_product(a, b, n):
    a.sort()
    b.sort()
    ans = sum([a[i]*b[i] for i in range(n)])
    return ans

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    print(max_dot_product(a, b, n))
    
