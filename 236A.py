if __name__ == '__main__':
    value = input()
    elems = set(value)
    print('CHAT WITH HER!' if len(elems)%2 == 0 else 'IGNORE HIM!')