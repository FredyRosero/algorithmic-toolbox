# Uses python3
import sys
import math

def get_change(money):
    denominations = [1, 3, 4]
    minCoins = [0] + [math.inf]*money

    for i in range(1, money+1):
        for j in denominations:
            if i>=j:
                coins = minCoins[i-j]+1
                if coins < minCoins[i]:
                    minCoins[i] = coins

    return(minCoins[money])

if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
