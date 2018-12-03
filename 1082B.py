if __name__ == '__main__':
    l = int(input())
    strV = input()
    array = [0 for i in range(l)]
    array[0] = 1 if strV[0] == 'G' else 0

    for i in range(1,l):
        array[i] = array[i-1] + 1 if strV[i] == 'G' else 0

    print(array)

