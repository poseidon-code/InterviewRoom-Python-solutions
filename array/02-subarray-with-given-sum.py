# PROBLEM: Subarray with given sum
# https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

from typing import List

# SOLUTION
def subarray_sum(A: List[int], S: int, N: int) -> List[int]:
    sum=A[0]
    start=0
    end=1

    while end<=N:
        while sum>S and start<end-1:
            sum = sum - A[start]
            start+=1
    
        if sum == S:
            return [start+1, end]

        if end < N:
            sum = sum + A[end]

        end+=1
    
    return [-1]


if __name__ == "__main__":
    # INPUT :
    A = [1,2,3,7,5]
    S = 12
    N = len(A)

    # OUTPUT :
    ss = subarray_sum(A,S,N)
    for p in ss:
        print(p, end=' ')
    print()