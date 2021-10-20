# PROBLEM: Check if binary tree is balanced
# https://leetcode.com/problems/balanced-binary-tree/


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
def traverse (root: Node) -> int:
    if root==None : return 0
    return max(traverse(root.left), traverse(root.left))+1

def is_balanced (root: Node) -> bool:
    if root==None : return True

    l = traverse(root.left)
    r = traverse(root.right)
    
    return abs(l-r) <= 1 and is_balanced(root.left) and is_balanced(root.right)



if __name__ == "__main__":
    # INPUT :
    elements = [9,3,20,None,None,15,7]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(is_balanced(root))