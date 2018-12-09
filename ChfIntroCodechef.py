
if __name__ == '__main__':
    val = [int(m) for m in input().split()]
    for i in range(val[0]):
        score = int(input())
        print('Good boi' if score >= val[1] else 'Bad boi')