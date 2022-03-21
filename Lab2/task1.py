#task 1
if __name__ == '__main__':
    L = ' '
    for el in range(500, 3001):
        if el % 7 == 0 and el % 5 != 0:
            L += str(el)
    x = L.count("21")
    L.replace("21", "XX")
