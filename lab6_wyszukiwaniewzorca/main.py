if __name__ == '__main__':
    #f = open('1000_pattern.txt', 'r')
    with open('1000_pattern.txt') as txt:
        lines = [line for line in txt]
    counter = 0
    for x in range(len(lines)-1):
        for y in range(len(lines)-1):
            if(lines[x][y] == 'A' and lines[x][y+1] == 'B' and lines[x][y+2] == 'C' and lines[x+1][y] == 'B' and lines[x+2][y] == 'C'):
                    print(x,y)
                    counter += 1
    print (f'liczba wystąpień wzorca {counter}')