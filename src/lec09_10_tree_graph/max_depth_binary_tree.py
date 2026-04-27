class Node:
    def __init__ (self, val = " ", left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__ (self):
        return str(self.val)

def max_depth(node):
    if node is None:
        return 0
    
    left_max = max_depth(node.left) if node.left else 0
    right_max = max_depth(node.right) if node.right else 0
    
    return max(left_max, right_max) + 1
    
    
def main():
    # 第一层
    A = Node("A")
    
    # 第二层
    B = Node("B"); C = Node("C"); A.left = B; A.right = C
    
    # 第三层
    D = Node("D"); E = Node("E"); F = Node("F"); G = Node("G")
    
    B.left = D; B.right = E; C.left = F; C.right = G
    
    # 第四层
    H = Node("H");I = Node("I"); J = Node("J")
    
    E.left = H; E.right = I; G.right = J
    print(f"Max Depth is: {max_depth(A)}")


main()