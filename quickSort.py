def quickSort(A,l,r): #l to lewy skrajny element listy, r to element na lewo od pivota
    if l < r:
        p = partition(A,l,r)
        quickSort(A,l,p - 1)
        quickSort(A,p + 1,r)
        

def partition(A,l,r):
    i = l #i to aktualna pozycja indeksu idącego od lewej, poszukującego wartości większych od pivota
    j = r - 1 #j to aktualna pozycja indeksu idącego od prawej, poszukującego wartości mnieszych od pivota
    pivot = A[r]
    while i < j:
        while i < r and A[i] < pivot:
            i += 1
        while j > l and A[j] >= pivot:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    
    if A[i] > pivot:
        A[i], A[r] = A[r], A[i]
    
    return i

X=[22,11,88,66,55,77,33,44]
quickSort(X,0,len(X) - 1)
print(X)
