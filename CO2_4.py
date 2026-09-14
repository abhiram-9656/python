#generate a list four digit numbers in a given range with all their digit even and the number is a perfect square
import math
for i in range(1000,10000):
    sqroot=int(math.sqrt(i))
    if sqroot*sqroot==i:
        num=str(i)
        if all(int(digit)%2==0 for digit in str(i)):
            print(i)
