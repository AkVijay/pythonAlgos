
if __name__ == '__main__':
    count = int(input())
    array = []
    for i in range(count):
        value = [int(i) for i in input().split()]
        maxV = max(value)
        array.append(maxV)
    for i in range(len(array)):
        if array[i] == count - 1:
            array[i] = count
            break
    for elem in array:
        print(elem, end=" ")
