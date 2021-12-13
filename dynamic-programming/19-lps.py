# PROBLEM: Longest palindromic subsequence
# https://leetcode.com/problems/longest-palindromic-subsequence/


# SOLUTION
def lps (s: str) -> int:
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            dp[i][j] = 2+dp[i+1][j-1] if s[j]==s[i] else max(dp[i+1][j], dp[i][j-1])

    return dp[0][n-1]


if __name__ == "__main__":
    # INPUT :
    s = "bbbab"

    # OUTPUT :
    print(lps(s))