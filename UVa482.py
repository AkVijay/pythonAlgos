
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        input()
        array_index = [int(v) for v in input().split()]
        array_floating = [v for v in input().split()]

        dict = {}
        i = 0
        for elem in array_index:
            dict[elem] = i
            i = i + 1

        for k in range(1,len(array_index)+1):
            print(array_floating[dict[k]])
        print()



