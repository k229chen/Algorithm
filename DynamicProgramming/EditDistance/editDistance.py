import time
def editDistanceREC(X, Y, m, n):
    global L
    if L[m-1][n-1] != None:
        return L[m-1][n-1]
    if m == 0:
        L[m-1][n-1] = n
        return L[m-1][n-1]
    if n == 0:
        L[m-1][n-1] = m
        return L[m-1][n-1]

    if X[m-1] == Y[n-1]:
        L[m-1][n-1] =  editDistanceREC(X, Y, m-1, n-1)
    else:
        L[m-1][n-1] = 1 + min(editDistanceREC(X, Y, m, n-1),
                editDistanceREC(X, Y, m-1, n-1),
                editDistanceREC(X, Y, m-1, n))
    return L[m-1][n-1]

str1 = 'intentzdjeidjascmiqmfjlznvqojpvvzl,qenvurqiondsjdjasldja'
str2 = 'execsaldjqwuzmcpkqiocqinvyzbkvnq,nvu bqndnqin zmcoqetion3njwqicq'

#str1 = 'sunday'
#str2 = 'saturday'

#str1 = 'un'
#str2 = 'atur'

global L

def editDistanceDP(X, Y):
    m = len(X)
    n = len(Y)
    global L

    L = [[None]*n for i in range(m)]

    return editDistanceREC(X, Y, m, n)

def editDistance(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                L[i][j] = j
            elif j == 0:
                L[i][j] = i
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]
            else:
                L[i][j] = 1 + min(L[i-1][j], L[i][j-1], L[i-1][j-1])

    return L[m][n]

T1s = time.time()
res1 = editDistanceDP(str1, str2)
T1e = time.time()

print 'up-bottom ', res1, T1e-T1s

T2s = time.time()
res2 = editDistance(str1, str2)
T2e = time.time()

print 'bottom-up ', res2, T2e-T2s 
