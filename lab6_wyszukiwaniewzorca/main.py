#d = 16
def rabin_karp_matcher(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q
    p = 0
    t = 0
    result = []
    for i in range(m):
        p = (d * p + ord(P[i])) % q
        t = (d * t + ord(T[i])) % q
    for s in range(n-m+1):
        if p == t:
            match = True
            for i in range(m):
                if P[i] != T[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
                print(f'wzorzec na ideksie: {s}')
        if s < n - m:
            t = (t - h * ord(T[s])) % q
            t = (t * d + ord(T[s + m])) % q
            t = (t + q) % q
    return result
if __name__ == '__main__':
    #f = open('1000_pattern.txt', 'r')
    with open('1000_pattern.txt') as txt:
        lines = [line for line in txt]
    counter = 0
    for x in range(len(lines)-1):
        for y in range(len(lines)-1):
            if(lines[x][y] == 'A' and lines[x][y+1] == 'B' and lines[x][y+2] == 'C' and lines[x+1][y] == 'B' and lines[x+2][y] == 'C'):
                    #print(x,y)
                    counter += 1
    print (f'liczba wystąpień wzorca {counter}')

    print(rabin_karp_matcher("3141592653589793", "26", 257, 11))
