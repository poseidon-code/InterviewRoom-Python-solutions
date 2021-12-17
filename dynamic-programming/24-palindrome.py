# PROBLEM: Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning-ii/


# SOLUTION
def min_cut (s: str) -> int:
    n = len(s)
    cut = [0]*(n+1)
    for i in range(n+1) : cut[i] = i-1

    for i in range(n):
        j = 0
        while i-j>=0 and i+j<n and s[i-j]==s[i+j]:
            cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j])
            j+=1
        
        j = 1
        while i-j+1>=0 and i+j<n and s[i-j+1]==s[i+j]:
            cut[i+j+1] = min(cut[i+j+1], 1+cut[i-j+1])
            j+=1

    return cut[n]


if __name__ == "__main__":
    # INPUT :
    s = "aab"

    # OUTPUT :
    print(min_cut(s))