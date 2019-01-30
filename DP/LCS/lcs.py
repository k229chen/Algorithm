def lcs(X, Y, lenX, lenY):
    if lenX == 0 or lenY == 0:
        return 0
    elif X[lenX-1] == Y[lenY-1]:
        return 1 + lcs(X, Y, lenX-1, lenY-1)
    else:
        return max(lcs(X,Y, lenX-1, lenY), lcs(X,Y, lenX, lenY-1))

X = "AGGTAB"
Y = "GXTXAYB"

print lcs(X, Y, len(X), len(Y))
