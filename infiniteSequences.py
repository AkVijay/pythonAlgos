
if __name__ == '__main__':
    values = [int(x) for x in input().split()]

    if values[2] == 0 :
        print('YES' if values[0] == values[1] else 'NO')
    else:
        print('YES' if (values[1]-values[0])//(values[2]) >= 0 and (values[1]-values[0])%(values[2]) == 0 else 'NO')
