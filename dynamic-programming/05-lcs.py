# PROBLEM: Longest common subsequence (delete operation for two strings)
# https://leetcode.com/problems/delete-operation-for-two-strings/


# SOLUTION
INT_MAX = 2**16
def lcs (word1: str, word2: str) -> int: 
    m, n = len(word1), len(word2)
    dp = [[0]*(n+1)]*(m+1)

    for i in range(m):
        for j in range(n):
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], dp[i][j]+(word1[i]==word2[j]))

    return m + n - 2 * dp[m][n]


if __name__ == "__main__":
    # INPUT :
    word1 = "sea"
    word2 = "eat"

    # OUTPUT :
    print(lcs(word1, word2))