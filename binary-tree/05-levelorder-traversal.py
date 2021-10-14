# PROBLEM: Level order traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal/


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
def levelorder (root: Node) -> List[List[int]]:
    q = []
    result = [[]]
    c = []

    if root==None : return result

    q.append(root)
    q.append(None)

    while len(q)!=0:
        t = q.pop(0)

        if t==None:
            result.append(c)
            c = []

            if len(q) > 0 : q.append(None)
        else:
            c.append(t.data)
            if t.left!=None : q.append(t.left)
            if t.right!=None : q.append(t.right)

    return result



if __name__ == "__main__":
    # INPUT :
    elements = [3,9,20,None,None,15,7]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    result = levelorder(root)
    print("[", end="")
    for x in result:
        if len(x)==0 : continue
        print("[", end="")
        for y in x:
            if y==None: continue
            print(y, end=",")
        print("\b]", end=",")
    print("\b]")