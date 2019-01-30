
def lcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None]*(n+1) for i in xrange(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1]+1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    traceLCS(X, Y, L)
    return L[m][n]

def traceLCS(X, Y, L):
    m = len(X)
    n = len(Y)
    lcs = ''

    while m != 0 and n != 0:
        if X[m-1] == Y[n-1]:
            lcs = X[m-1] + lcs
            m -= 1
            n -= 1
        elif L[m-2][n-1] > L[m-1][n-2]:
            m -= 1
        else:
            n -= 1
    print lcs

def helper(X, Y, m, n, L):
    if L[m][n] != None:
        return L[m][n]
    if m == 0 or n == 0:
        L[m][n] = 0
    elif X[m-1] == Y[n-1]:
        L[m][n] = 1 + helper(X, Y, m-1, n-1, L)
    else:
        L[m][n] = max(helper(X, Y, m-1, n, L), helper(X, Y, m, n-1, L))
    return L[m][n]
'''
def lcs(X, Y):
m = len(X)
n = len(Y)

    L = [[None]*(n+1) for i in xrange(m+1)]

    return helper(X, Y, len(X), len(Y), L)
'''
X = "MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCALLAAQANKESSSESFISRLLAIVAD"
Y = "MAEEEVAKLEKHLMLLRQEYVKLQKKLAETEKRCTLLAAQANKENSNESFISRLLAIVAG"

print X
print Y
lcs(X, Y)
