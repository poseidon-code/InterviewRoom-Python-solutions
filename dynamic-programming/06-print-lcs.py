# PROBLEM: Print longest common subsequence
# https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem


from typing import List

# SOLUTION
def lcs (A: List[int], B: List[int]) -> List[int]:
    C = []
    n, m = len(A), len(B)
    for i in range(n+1):
        C.append([])        
        for j in range(m+1):
            C[-1].append([])
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if A[i-1] == B[j-1]:                                                    
                C[i][j] = C[i-1][j-1] + [A[i-1]]
            else:
                C[i][j] = C[i-1][j] if len(C[i-1][j]) >= len(C[i][j-1]) else C[i][j-1]

    return C[n][m]


if __name__ == "__main__":
    # INPUT :
    A = [1,2,3,4,1]
    B = [3,4,1,2,1,3]

    # OUTPUT :
    print(lcs(A, B))