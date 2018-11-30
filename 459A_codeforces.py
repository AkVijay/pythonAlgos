if __name__ == '__main__':
    value = [int(m) for m in input().split()]

    x1 = value[0]
    x2 = value[2]
    y1 = value[1]
    y2 = value[3]

    if not (y2 - y1 == 0
            or x2 - x1 == 0
            or abs(y2-y1) == abs(x2-x1)):
        print(-1)
    else:
        if y2 - y1 == 0:
            print(str(x1) + " " + str(y1 + abs(x2-x1)) + " " + str(x2) + " " + str(y2 + abs(x2-x1)))
        if value[2] - value[0] == 0:
            print(str(x1 + abs(y2-y1)) + " " + str(y1) + " " + str(x2 + abs(y2-y1)) + " " + str(y2))
        if abs(value[1]-value[3]) == abs(value[2]-value[0]):
            print(str(x1) + " " + str(y2) + " " + str(x2) + " " + str(y1))

