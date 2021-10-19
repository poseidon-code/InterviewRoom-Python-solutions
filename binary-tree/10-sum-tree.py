# PROBLEM: Check if sum tree
# https://practice.geeksforgeeks.org/problems/sum-tree/1


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
result = True
def traverse (root: Node) -> int:
    if root==None : return 0
    if root.left==None and root.right==None : return root.data

    ld = traverse(root.left)
    rd = traverse(root.right)
    global result

    if ld+rd!=root.data : result = False

    return root.data+ld+rd

def is_sum_tree (root: Node) -> bool:
    traverse(root)
    return result



if __name__ == "__main__":
    # INPUT :
    elements = [10,20,30,10,10]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(is_sum_tree(root))