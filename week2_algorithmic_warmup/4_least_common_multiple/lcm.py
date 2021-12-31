# Uses python3
import sys

# This function computes GCD 
def gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def lcm(x, y):
   lcm = (x*y)//gcd(x,y)
   return lcm


if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm(a, b))

