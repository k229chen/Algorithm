global maximum
maximum = 1
def lisREC(X, m):
    global maximum
    lisAtM = 1
    if m == 1:
        return 1

    for i in range(1, m):
        lisAtI = lisREC(X, i)
        if lisAtI + 1 > lisAtM and X[i-1] < X[m-1]:
            lisAtM = lisAtI + 1

    maximum = max(maximum, lisAtM)
    return lisAtM

#X = [3, 10, 2, 1, 20]
X = [50, 3, 10, 7, 40, 80]
#X = [10, 22, 9, 33, 21, 50, 41, 6]
#X = [3, 2]

#print(lisREC(X, len(X)))
#print(maximum)


def lisDP(X):
    m = len(X)
    
    L = [1]*m
    
    for i in range(m):
        for j in range(i):
            if X[j] < X[i] and L[j] + 1 > L[i]:
                L[i] = L[j] + 1

    return max(L)

print(lisDP(X))
