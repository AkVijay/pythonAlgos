

from collections import deque

if __name__ == '__main__':

    while True:
        value = input()
        if value == '':
            break

        q = deque()

        sample_q = []

        toggle = False

        i = 0

        for elem in value:
            i += 1
            if elem == '[' or elem == ']':
                toggle = True if elem == '[' else False
                val = ''.join(sample_q)
                q.appendleft(val)
                sample_q = []
                continue

            if not toggle:
                q.append(elem)
            else:
                sample_q.append(elem)

        if len(sample_q) > 0:
            q.appendleft(''.join(sample_q))

        while len(q) > 0:
            print(q.popleft(), end='')
        print()
