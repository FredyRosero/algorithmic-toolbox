# Uses python3
import sys

def get_majority_element(seq, l, r):
    if l+1==r:
        return seq[l]
    elif l+2==r:
        return seq[l]
    m = (l+r)//2
    left = get_majority_element(seq, l, m)
    right = get_majority_element(seq, m, r)

    c1, c2 = 0, 0
    for i in seq[l:r]:
        if i == left:
            c1+=1
        elif i == right:
            c2+=1
    if c1>(r-l)//2 and left != -1:
        return left
    elif c2>(r-l)//2 and right != -1:
        return right
    else: 
        return -1

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
