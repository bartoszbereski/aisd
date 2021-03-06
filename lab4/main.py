def insertionsort(A):
    for i in range(1,len(A)):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = x
def mergesort(A, a,b):
    if a < b:
        c = (a+b)/2
        mergesort(A, a,c)
        mergesort(A, c+1, b)
        merge(A, a, c, b)
def merge(A: list, start: int, mid: int, end: int) -> None:
         tmp = []
         i = start
         j = mid + 1
         k = 0
         while i <= mid and j <= end:
             if A[i] <= A[j]:
                 tmp.append(A[i])
                 k += 1
                 i += 1
             else:
                 tmp.append(A[j])
                 k += 1
                 j += 1
         while i <= mid:
             tmp.append(A[i])
             k += 1
             i += 1
         while j <= end:
             tmp.append(A[j])
             k += 1
             j += 1
         for i in range(start, end + 1):
             A[i] = tmp[i - start]
if __name__ == '__main__':
    A = [3,2,1,4,5,6,2,5]
    A1 = [3,2,1,4,5,6,2,5]
    insertionsort(A)
    print(A)