# PROBLEM: Postorder traversal
# https://www.interviewbit.com/problems/postorder-traversal/


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
def postorder (root: Node) -> List[int]:
    s = []
    result = []
    last = Node()

    if root==None : return result

    while len(s)!=0 or root!=None:
        if root!=None:
            s.append(root)
            root = root.left
        else:
            temp = s[-1]

            if temp.right!=None and last!=temp.right:
                root = temp.right
            else:
                result.append(temp.data)
                last = temp
                s.pop()

    return result



if __name__ == "__main__":
    # INPUT :
    elements = [1,None,2,None,None,3,None]
    root = NBT(elements, Node(elements[0]), 0, len(elements))

    # OUTPUT :
    result = postorder(root)
    print("[", end="")
    for x in result:
        if x==None: continue
        print(x, end=" ")
    print("\b]")