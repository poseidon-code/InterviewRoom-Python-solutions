# PROBLEM: Right view of binary tree
# https://leetcode.com/problems/binary-tree-right-side-view/


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
def right_view (root: Node) -> List[int]:
    q = []
    result = []

    if root==None : return result

    q.append(root)

    while len(q)!=0:
        size = len(q)

        for i in range(size):
            t = q.pop(0)
            if i==size-1 : result.append(t.data)
            if t.left!=None : q.append(t.left)
            if t.right!=None : q.append(t.right)

    return result



if __name__ == "__main__":
    # INPUT :
    elements = [1,2,3,None,5,None,4]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    result = right_view(root)
    print("[", end="")
    for x in result:
        if x==None: continue
        print(x, end=" ")
    print("\b]")