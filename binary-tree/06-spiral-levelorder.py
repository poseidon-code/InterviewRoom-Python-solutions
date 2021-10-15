# PROBLEM: Level order traversal in sipral form
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# https://www.interviewbit.com/problems/zigzag-level-order-traversal-bt/

from typing import List

class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def NBT (elements, root, i, n) -> Node:
    if n==0 : return None

    if i<n:
        temp = Node(elements[i])
        root = temp
        root.left = NBT(elements, root.left, 2*i+1, n)
        root.right = NBT(elements, root.right, 2*i+2, n)

    return root


# SOLUTION
def levelorder_spiral (root: Node) -> List[List[int]]:
    q = []
    result = [[]]
    l2r = True

    if root==None : return result

    q.append(root)

    while len(q)!=0:
        s = len(q)
        row = [None]*s

        for i in range(s):
            t = q.pop(0)
            
            index = i if l2r else s-1-i

            row[index] = t.data
            if t.left!=None : q.append(t.left)
            if t.right!=None : q.append(t.right)

        l2r = not(l2r)
        result.append(row)

    return result



if __name__ == "__main__":
    # INPUT :
    elements = [3,9,20,None,None,15,7]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    result = levelorder_spiral(root)
    print("[", end="")
    for x in result:
        if len(x)==0 : continue
        print("[", end="")
        for y in x:
            if y==None: continue
            print(y, end=",")
        print("\b]", end=",")
    print("\b]")