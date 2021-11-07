# PROBLEM: Inorder successor in BST
# https://practice.geeksforgeeks.org/problems/inorder-successor-in-bst/1


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
def inorder_successor (root: Node, x: Node) -> Node:
    if root==None : return None
    s = None

    while(root):
        if(root.data<=x.data):
            root=root.right
        elif(root.data>x.data):
            s=root
            root=root.left
        else:
            break

    return s


if __name__ == "__main__":
    # INPUT :
    elements = [2,1,3]
    root = NBT(elements, Node(elements[0]), 0, len(elements))
    x = root.left

    # OUTPUT :
    print(inorder_successor(root, x).data)