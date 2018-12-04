

from collections import deque

if __name__ == '__main__':

    while True:
        n = int(input())
        if n == 0:
            print()
            break
        q = deque()

        for i in range(1,n+1):
            q.append(i)

        discarded_cards = []
        while len(q) > 1:
            elem1 = q.popleft()
            discarded_cards.append(elem1)
            elem2 = q.popleft()
            q.append(elem2)

        discarded_cards = [str(elem) for elem in discarded_cards]
        print('Discarded cards:' if n == 1 else 'Discarded cards: %s'%(', '.join(discarded_cards)))
        print('Remaining card: %s'%(q.popleft()))