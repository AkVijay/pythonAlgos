
if __name__ == '__main__':

    dict = {}
    while True:
        q = input()
        print(q)
        if q == "":
            print()
            break
        for elem in q.split():
            interm = elem.lower()
            if len(interm) > 1 and interm[-2] == "'" and interm[-1] == 's':
                interm = interm[:-2]

            copy_interm = [t if t.isalpha() else "" for t in interm]
            interm = "".join(copy_interm)
            dict[interm] = 1

    output = []
    for key,value in dict.items():
            output.append(key)

    output.sort()

    for elem in output:
        print(elem)



