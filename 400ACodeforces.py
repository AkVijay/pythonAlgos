

constants = [1,2,3,4,6,12]
constants.reverse()

if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        value = input()
        result = []

        for elem in constants:
            matrix = [[value[i] for i in range(k,k+elem)] for k in range(0,12, elem)]
            width = len(matrix[0])
            length = len(matrix)

            for i in range(width):
                matrix_found = True
                for j in range(length):
                    if matrix[j][i] == 'O':
                        matrix_found = False
                        break
                if matrix_found :
                    result.append(elem)
                    break

        print(len(result) , end = ' ')
        for elem in result:
            print(str(12//elem) +"x" + str(elem) , end = ' ')
        print()





































