
if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            print()
            break
        values = []
        for i in range(n):
            values.append(input())

        maxB = 1000000000000
        dictV = {}
        index = -1
        for i in range(n):
            countB = 0
            for j in range(25):
                if values[i][j] == ' ':
                    countB += 1
            dictV[i] = countB
            if countB < maxB:
                maxB = countB

        countF = 0
        for key,value in dictV.items():
            countF += value - maxB

        print(countF)






