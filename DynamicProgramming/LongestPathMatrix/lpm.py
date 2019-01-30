import time

def traceCell(M, m, n, dp, previous):
    if dp[m][n] != None:
        return dp[m][n]
    if m < 0 or n < 0:
        return 0
    if M[m][n] = previous + 1:
        return traceCell
    

def lpm(M):
    m = len(M)
    n = len(M[0])

    dp = [[None]*n for i in range(m)]

    for i in range(m):
        for j in range(n):
            res = 1 + max(traceCell(M, m+1, n, dp, M[m][n]),
                    traceCell(M, m, n+1, dp, M[m][n]),
                    traceCell(M, m-1, n, dp, M[m][n]),
                    traceCell(M, m, n-1, dp, M[m][n]))
