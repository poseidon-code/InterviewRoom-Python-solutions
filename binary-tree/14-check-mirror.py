# PROBLEM: Check if 2 binary trees are mirror of each other
# https://practice.geeksforgeeks.org/problems/check-mirror-in-n-ary-tree1528/1


from typing import List

# SOLUTION
def check_mirror (n: int, e: int, A: List[int], B: List[int]) -> bool:
    mp={}
    
    i=0
    while(i<(e*2)):
        if A[i] not in mp:
            mp[A[i]] = [A[i+1]]
        else:
            mp[A[i]].append(A[i+1])
        i+=2
    
    i=0
    while(i<(2*e)):
        if mp[B[i]][-1] != B[i+1]:
            return False
        mp[B[i]].pop()
        i+=2
    
    return True


if __name__ == "__main__":
    # INPUT :
    n = 3
    e = 2
    A = [1,2,1,3]
    B = [1,3,1,2]

    # OUTPUT :
    print(check_mirror(n, e, A, B))