import sys

def burger_time(length , elem):

    prev_restaurant = -1
    prev_drug_store = -1
    diff = sys.maxsize

    i = -1
    for v in elem:

        i = i + 1

        if v == '.':
            continue

        if v == 'Z':
            return 0

        if v == 'D':
            prev_drug_store = i
            if prev_restaurant != -1:
                diff = min(diff, abs(prev_restaurant-prev_drug_store))

        if v == 'R':
            prev_restaurant = i
            if prev_drug_store != -1:
                diff = min(diff, abs(prev_restaurant-prev_drug_store))

    return diff

if __name__ == '__main__':
    while True :
        value = int(input())
        if value == 0:
            break
        else:
            value2 = input()
            print(burger_time(value, value2))