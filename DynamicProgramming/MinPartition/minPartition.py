import time

def minPartition(L):
    n = len(L)

    dp = [[0]* n for i in range(n+1)]

    total = abs(sum(L))

    minAbs = total
    L2 = L * 2

    for i in range(n+1):
        for j in range(n):
            if i == 0:
                dp[i][j] = total
            else:
                dp[i][j] = dp[i-1][j] - 2*L2[j+i]
                if abs(dp[i][j]) < minAbs:
                    minAbs = abs(dp[i][j])
    return minAbs


L = [3,1,4,2,2,1]

print minPartition(L)
