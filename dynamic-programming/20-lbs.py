# PROBLEM: Longest Bitonic Subsequence
# https://www.interviewbit.com/problems/length-of-longest-subsequence/


from typing import List

# SOLUTION
def lbs (A: List[int]) -> int:
    n = len(A)
    
    lis = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if A[i]>A[j] and lis[i]<lis[j]+1:
                lis[i] = lis[j]+1

    lds = [1]*n
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if A[i]>A[j] and lds[i]<lds[j]+1:
                lds[i] = lds[j]+1
    
    result = lis[0] + lds[0] -1
    for i in range(1, n):
        if lis[i]+lds[i]-1 > result:
            result = lis[i] + lds[i] -1
    
    return result


if __name__ == "__main__":
    # INPUT :
    A = [1,2,1]

    # OUTPUT :
    print(lbs(A))