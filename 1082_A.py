
import sys

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        [n,x, y, d] = [int(m) for m in input().split()]


        if (y-x)%d == 0:
            print(abs(y-x)//d)

        elif (y - 1)%d == 0:
            count1 = ((y-1)//d + ((x-1)//d if (x-1)%d == 0 else (x-1)//d + 1))
            count2 = ((n-y)//d if (n-y)%d == 0 else sys.maxsize)  + (((n-x)//d) if (n-x)%d == 0 else (n-x)//d + 1)
            print(min(count1,count2))

        elif (n-y)%d == 0:
            print(((n-y)//d if (n-y)%d == 0 else sys.maxsize)  + (((n-x)//d) if (n-x)%d == 0 else (n-x)//d + 1))

        else:
            print(-1)
