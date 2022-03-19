from timeit import default_timer as timer
#task1
L=[1,2]
for i in range(2,48):
    L.append((L[i-1]+L[i-2])/(L[i-1]-L[i-2]))
print("avg=", sum(L)/len(L))
L.sort()
if len(L)%2!=0:
    print("mediana=", L[len(L)//2-1])
else:
    print("mediana=", (L[len(L)//2-1]+L[len(L)//2])/2)
counter = {}
for el in L:
    if el not in counter:
        counter[el]=1
    else:
        counter[el]+=1
print(counter)
#task 2
L1=[1,2]


#task3
start = timer()
word=[1,2,3,4,5]
for i in word:
    print(i)
end = timer()
print(end - start)
#from c++
start1=timer()
for i in range(1,6):
    print(i)
end1= timer()
print(end1 - start1)
#task4
#4.1
names=["tom","jerry","john","matt"]
try:
    print(names[4])
except:
    print("IndexError stopped")
#4.2
x=0
y=0
try:
    z = x / y
except:
    print("ZeroDivisionError")
#4.3
u=0
try:
    print(k)
except:
    print("NameError solved")