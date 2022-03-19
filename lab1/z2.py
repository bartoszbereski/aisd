
def main():
        L=[1,2]
        for i in range(2,48):
            L.append((L[i-1]+L[i-2])/(L[i-1]-L[i-2]))

        print(len(L))


if __name__=="__main__":
    main()