


if __name__ == '__main__':
    while True:
        value1 = [int(i) for i in input().split(" ")]
        if(value1[0] == 0):
             break

        current_reserves = [int(i) for i in input().split(" ")]

        for i in range(value1[0]):
            value = [int(i) for i in input().split(" ")]
            current_reserves[value[0]-1] -= value[2];
            current_reserves[value[1]-1] += value[2];

        current_reserves = [i < 0 for i in current_reserves]
        if any(current_reserves):
            print('N')
        else:
            print('S')