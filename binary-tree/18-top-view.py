# PROBLEM: Top view of binary tree
# https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1


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
def top_view (root: Node) -> Node:
    result = []
    q = [(root, 0)]
    m = {}

    while (q):
        x, p = q.pop(0)
        
        if x.left : q.append((x.left, p-1))
        if x.right : q.append((x.right, p+1))
        if p not in m : m[p] = x.data
    
    for i in sorted(m.keys()):
        result.append(m[i])
    
    return result



if __name__ == "__main__":
    # INPUT :
    elements = [1,2,3,4,5,6,7]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    print(top_view(root))