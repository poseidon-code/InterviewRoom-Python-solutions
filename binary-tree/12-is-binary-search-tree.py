# PROBLEM: Check if a binary tree is BST
# https://practice.geeksforgeeks.org/problems/check-for-bst/1


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
def traverse (root: Node, min: Node, max: Node) -> bool:
    if root==None : return True
    if min!=None and root.data<=min.data : return False
    if max!=None and root.data>=max.data : return False

    l = traverse(root.left, min, root)
    r = traverse(root.right, root, max)

    return l and r
    

def is_bst (root: Node) -> bool:
    return traverse(root, None, None)


if __name__ == "__main__":
    # INPUT :
    elements = [2,1,3]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(is_bst(root))