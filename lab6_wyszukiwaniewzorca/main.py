d = 16
q = 13
def rabin_karp_matcherhorizontal(T, P, d, q):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q
    result = set()
    for x in range(n - 2):
        p = 0
        t = 0
        for i in range(m):
            p = (d * p + ord(P[i])) % q
            t = (d * t + ord(T[x][i])) % q
        for s in range(n-m+1):
            if p == t:
                match = True
                for i in range(m):
                    if lines[x][s + i] != P[i]:
                        match = False
                        break
                if match:
                    result.add((x, s))
                    #print(f'wzorzec na ideksie: {s}')
            if s < n - m:
                t = ((t - h * ord(T[x][s])) * d + ord(T[x][s + m])) % q
    return result
def rabin_karp_matchervertical(T, P, d, q, result):
    n = len(T)
    m = len(P)
    h = pow(d, m - 1) % q
    finalresult = set()
    for x in range(n - 2):
        p = 0
        t = 0
        for i in range(m):
            p = (d * p + ord(P[i])) % q
            t = (d * t + ord(T[i][x])) % q
        for s in range(n-m+1):
            if p == t:
                match = True
                for i in range(m):
                    if (lines[s + i][x] != P[i]):
                        match = False
                        break
                if match and (s, x) in result:
                    finalresult.add((s, x))
            if s < n - m:
                t = ((t - h * ord(T[s][x])) * d + ord(T[s + m][x])) % q
    return finalresult
def rabin_karp_matcher(array, string):
    results_horizontal = rabin_karp_matcherhorizontal(array, string, 16, 13)
    results = rabin_karp_matchervertical(array, string, 16, 13, results_horizontal)
    return results
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
    #print (f'liczba wystąpień wzorca {counter}')
    patterns_found= len(rabin_karp_matcher(lines, "ABC"))
    print("patterns found: "+str(patterns_found))
