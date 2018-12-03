if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break

        matrix = []
        for i in range(n):
            val = [int(m) for m in input().split()]
            val.append(0)
            matrix.append(val)
        matrix.append([0 for i in range(n)])

        for i in range(n):
            for j in range(n):
                matrix[i][n] += matrix[i][j]
                matrix[n][j] += matrix[i][j]

        corrupt_columns = []
        corrupt_rows = []

        for i in range(n):
            if matrix[n][i]%2 != 0:
                corrupt_columns.append(i)

        for i in range(n):
            if matrix[i][n] % 2 != 0:
                corrupt_rows.append(i)

        if len(corrupt_rows) == 0 and len(corrupt_columns) == 0:
            print('OK')
        elif len(corrupt_rows) == 1 and len(corrupt_columns)== 1:
            print('Change bit (%s,%s)'%(corrupt_rows[0] + 1, corrupt_columns[0] + 1))
        else:
            print('Corrupt')