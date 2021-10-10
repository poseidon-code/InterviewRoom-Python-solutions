# PROBLEM: Inorder traversal
# https://www.interviewbit.com/problems/inorder-traversal/


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
def inorder (root: Node) -> List[int]:
    s = []
    result = []

    if root==None : return result

    c = root.left
    s.append(root)

    while len(s)!=0 or c!=None:
        while c!=None:
            s.append(c)
            c=c.left

        temp = s[-1]
        s = s[:-1]
        result.append(temp.data)
        c = temp.right

    return result



if __name__ == "__main__":
    # INPUT :
    elements = [1,6,2,None,None,3,None]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    result = inorder(root)
    print("[", end="")
    for x in result:
        if x==None: continue
        print(x, end=" ")
    print("\b]")