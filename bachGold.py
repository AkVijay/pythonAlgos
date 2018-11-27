
if __name__ == '__main__':
    value = int(input())
    if value%2 == 0:
        print(value//2)
        for i in range(value//2):
            print("2", end=" ")

    else:
        print((value-3)//2 + 1)
        for i in range((value-3)//2):
            print("2",end=' ')
        print('3')