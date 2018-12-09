
if __name__ == '__main__':

    while True:
        k = [int(m) for m in input().split()]
        all_zeros = [elem == 0 for elem in k]
        if all(all_zeros):
            print()
            break

        assert 1 <= k[0] <= 500
        assert 1 <= k[1] <= 500
        assert 1 <= k[2] <= 99

        count_array  = [[False for i in range(k[0])] for j in range[k[1]]]

        n = k[2]

        while n > 0:
            values = [int(m) for m in input()]
            x1 = values[0]
            y1 = values[1]
            x2 = values[2]
            y2 = values[3]



















