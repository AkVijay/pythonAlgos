if __name__ == '__main__':

    [n, c] = [input(m) for m in input().split()]
    coins_count = 1000

    output_found = False
    val = 0
    prev_result = 0
    high = n if n%2 == 0 else n + 1
    low = 0
    while True:
        if output_found:
            print(3, end=' ')
            print(val)
            break

        if prev_result == 1:
            k = (high + low)//2
            print(1, end=' ')
            print(k)



        coins_count -= 1
        result = int(input())

        if result == 0:
            output_found = True
            val = k

        elif result == 1:
            print(2)
            coins_count -= c










