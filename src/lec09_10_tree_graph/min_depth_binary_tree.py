class Node:
    def __init__ (self, val = " ", left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__ (self):
        return str(self.val)

def min_depth(node):
    if not node:
        return 0
     
    left_min = min_depth(node.left)
    right_min = min_depth(node.right) 
    
    if not node.left or not node.right:
        return 1 + max(left_min, right_min)

    return 1 + min(left_min, right_min)
    
    
def main():
    # 第一层
    A = Node("A")
    
    # 第二层
    B = Node("B"); C = Node("C"); A.left = B; A.right = C
    
    # 第三层
    D = Node("D"); E = Node("E"); F = Node("F"); G = Node("G")
    
    #remove F compare to other test case
    B.left = D; B.right = E; C.right = G # C.left = F;
    
    # 第四层
    H = Node("H");I = Node("I"); J = Node("J")
    
    E.left = H; E.right = I; G.right = J
    print(f"Min Depth is: {min_depth(A)}")


main()