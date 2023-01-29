def insSort(A):
    for akt in range(1,len(A)):
        print(akt)
        print(A)
        while A[akt - 1] > A[akt] and akt > 0:
            A[akt - 1], A[akt] = A[akt], A[akt - 1]
            print(A)
            akt = akt - 1

#przykladowe sortowanie tablicy
X = [3,5,6,1,2,4]
insSort(X)