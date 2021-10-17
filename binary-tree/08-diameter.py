# PROBLEM: Diameter of binary tree
# https://leetcode.com/problems/diameter-of-binary-tree/


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
d = 0
def traverse (root: Node) -> int:
    if root==None : return 0
    ld = traverse(root.left)
    rd = traverse(root.right)
    global d 
    d = max(d, ld+rd)
    return max(ld, rd)+1

def diameter (root: Node) -> int:
    traverse(root)
    return d



if __name__ == "__main__":
    # INPUT :
    elements = [1,2,3,4,5]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(diameter(root))