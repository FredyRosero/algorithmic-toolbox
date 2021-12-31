# Uses python3
import sys
import random

def partition3(a, l, r):
    #Divide and conquer
    x = a[l]
    m1 = l
    m2 = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            a[i],a[m1] = a[m1],a[i]
            m1+=1
            m2+=1
            a[i],a[m2] = a[m2],a[i]
        elif a[i] == x:
            m2+=1
            a[i],a[m2] = a[m2],a[i]
   # a[l],a[m1] = a[m1],a[l]
    return m1,m2    	

def randomized_quick_sort(a, l, r):
    if l + 1 >= r:
        return

    k = random.randint(l, r - 1)

    a[l], a[k] = a[k], a[l]

    m1,m2 = partition3(a, l, r)
    
    randomized_quick_sort(a, l, m1)
    randomized_quick_sort(a, m2 + 1, r)


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
