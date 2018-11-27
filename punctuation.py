
if __name__ == '__main__':
    value = input()
    result = []
    for i in range(len(value)):
        if value[i].islower():
            result.append(value[i])

        elif value[i] == ' ':
            if result[-1] == ' ':
                continue
            else:
              result.append(' ')

        else:
            #punctuation
            if result[-1] == ' ':
                result.pop()
            result.append(value[i])
            result.append(' ')
    result = "".join(result)
    print(result)

