
if __name__ == '__main__':
    q = int(input())
    for i in range(q):
        exp = input()

        stack1 = []
        stack2 = []

        for elem in exp:
            if elem == '(':
                continue
            elif elem == ')':
                elem1 = stack1.pop()
                elem2 = stack1.pop()
                operator = stack2.pop()
                stack1.append(elem2+elem1+operator)

            elif elem == '*' or elem == '+' or elem == '/' or elem == '-' or elem == '^':
                stack2.append(elem)

            else:
                stack1.append(elem)

        print(stack1.pop())
