# PROBLEM: Delete node from BST
# https://leetcode.com/problems/delete-node-in-a-bst/


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
def delete_node (root: Node, value: int) -> Node:
    if not root : return root

    if root.data > key:
        root.left = delete_node(root.left, key)
    elif root.data < key:
        root.right = delete_node(root.right, key)
    else:
        if not root.right : return root.left
        if not root.left : return root.right
        
        temp = root.right
        while temp.left:
            temp = temp.left
        
        root.data = temp.data
        root.right = delete_node(root.right,root.data)
    
    return root


if __name__ == "__main__":
    # INPUT :
    elements = [5,3,6,2,4,None,7]
    key = 3
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    delete_node(root, key)