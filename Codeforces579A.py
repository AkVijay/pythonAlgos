
if __name__ == '__main__':
    val = int(input())
    count = 0
    for i in range(32):
        count += 1 if val & 1 << i else 0
    print(count)