
from functools import reduce

if __name__ == '__main__':
    value = [int(m) for m in input().split()]
    value = reduce(lambda x, y: x+y, value)
    print(value//5 if value > 0 and value%5 == 0 else -1)

