if __name__ == '__main__':
    while True:
        n = int(input())
        if n == 0:
            break
        while True:
            val = [int(m) for m in input().split()]
            if val[0] == 0:
                print()
                break

            stack = []
            coaches = 1

            i = 0
            while coaches <= n:
                stack.append(coaches)

                while len(stack) > 0 and stack[-1] == val[i]:
                    i += 1
                    stack.pop()

                coaches += 1
            print('Yes' if len(stack) == 0 else 'No')