

if __name__ == '__main__':

    while True:
        n = int(input())
        if n == 0:
            break
        a = b = 0

        turn = True
        for i in range(32):
            if (1 << i) & n:
                if turn:
                    a = a | 1 << i
                else:
                    b = b | 1 << i
                turn = not turn
        print(str(a) + " " + str(b))



