
import functools

if __name__ == '__main__':
    value1 = [int(x) for x in input().split()]
    value2 =[int(x) for x in input().split()]
    value3 = input()
    value3 = int(value3)

    value1 = functools.reduce(lambda x, y: x + y, value1)
    value2 = functools.reduce(lambda x, y: x + y, value2)

    count1 = value1//5
    value1 = value1 - 5 * count1
    count1 += 1 if value1%5 > 0 else 0

    count2 = value2//10
    value2 = value2 - 10 * count2
    count2 += 1 if value2%10 > 0 else 0

    print('YES' if count1 + count2 <= value3 else 'NO')

