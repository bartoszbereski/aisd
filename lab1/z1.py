from statistics import median


def main():
        L=[1,2]
        for i in range(2,48):
            L.append((L[i-1]+L[i-2])/(L[i-1]-L[i-2]))
        avg=sum(L)/len(L)
        L.sort()
        if len(L)%2==0:
           print("mediana",(L[(len(L)//2)-1]+L[(len(L)//2)])/2)
        else:
            print("mediana=",L[(len(L)//2)-1])
        print("avg=",avg)
        #print("median=",median(L))
        print(L)
        flag=True
        for despacito in L:
            if L.count(despacito)>1:
                print(despacito)
                flag=False
        if flag:
            print("nie znaleziono elementu sadge")



if __name__=="__main__":
    main()