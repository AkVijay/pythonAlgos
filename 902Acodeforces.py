
if __name__ == '__main__':
    values = [int(m) for m in input().split()]
    dict ={}
    for i in range(values[0]):
        ranges = [int(m) for m in input().split()]
        for value in range(ranges[0], ranges[1]):
            dict[value] = value + 1
        way_found = True
        for i in range(0,values[1]):
            if not (i in dict):
                way_found = False
    print('YES' if way_found else 'NO')
