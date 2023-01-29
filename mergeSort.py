def mergeSort(A):
    if len(A) > 1:
        #podzial tablicy na pol
        L = A[:len(A)//2]
        R = A[len(A)//2:]
        #rekursja
        mergeSort(L)
        mergeSort(R)
        #scalenie(merge)
        l = 0 #indeks lewej tablicy
        r = 0 #indeks prawej tablicy
        s = 0 #indeks scalonej tablicy
        while l < len(L) and r < len(R):
            if L[l] < R[r]:
                A[s] = L[l]
                l += 1
            else:
                A[s] = R[r]
                r += 1
            s += 1
        while l < len(L):
            A[s] = L[l]
            l += 1
            s += 1
        while r < len(R):
            A[s] = R[r]
            r += 1
            s += 1

X = [1,4,6,7,8,2,4,8,9,4,2,7,1,2,5,4,8,9]
mergeSort(X)
print(X)
