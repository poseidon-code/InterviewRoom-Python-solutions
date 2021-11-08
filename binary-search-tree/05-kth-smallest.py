# PROBLEM: kth smallest node in BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/


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

result, value = 0, 0

def traverse (root: Node):
    if not root or not root.data : return
    traverse(root.left)
    global value, result
    value-=1
    if value==0 : result = root.data
    traverse(root.right)


# SOLUTION
def kth_smallest (root: Node, x: Node) -> Node:
    global value
    value = k
    traverse(root)
    return result    


if __name__ == "__main__":
    # INPUT :
    elements = [3,1,4,None,2]
    k = 1
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(kth_smallest(root, k))