from time import time
if __name__ == '__main__':
   f = open('sjp.txt', 'r')
   x=input().strip().lower()
   start = time()
   if x.count(' ') == 0:
      print('jeden wyraz')
      if x in open('sjp.txt').read():
         print("jest takie slowo")
         slownik = open('SJP.txt', encoding='utf-8').read().splitlines()
         print(x)
      else:
         print("nie ma takiego slowa")
         slownik = open('SJP.txt', encoding='utf-8').read().splitlines()
         print(x)
   else:
      print("wiecej niz jeden wyraz")
   end = time()
   print("execution time: ",end-start)
   f.close()