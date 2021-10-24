# PROBLEM: Symmetric tree
# https://leetcode.com/problems/symmetric-tree/
# https://www.interviewbit.com/problems/symmetric-binary-tree/


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
def traverse (p: Node, q: Node) -> bool:
    if p==None and q==None : return True
    elif p==None or q==None : return False

    if p.data != q.data : return False

    return traverse(p.left, q.right) and traverse(p.right, q.left)
    
def is_symmetric (root: Node) -> bool:
    if root==None : return True
    return traverse(root.left, root.right)


if __name__ == "__main__":
    # INPUT :
    elements = [1,2,2,3,4,4,3]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(is_symmetric(root))