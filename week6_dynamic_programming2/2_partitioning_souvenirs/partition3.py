# Uses python3
import sys
import numpy

def partition3(W, n, items):
    count = 0 
    value = numpy.zeros((W+1, n+1))
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
            if value[i][j] == W: count += 1

    if count < 3: return '0'
    else: return '1'

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    total_weight = sum(A)
    if n<3: 
        print('0')
    elif total_weight%3 != 0: 
        print('0')
    else:
        print(partition3(total_weight//3, n, A))

