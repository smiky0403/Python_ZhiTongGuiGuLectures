class Node:
    def __init__(self, val = "", left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return str(self.val)


def pre_order_traversal(node):
    if node is None:
        return 
    print(node, end =" ")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def in_order_traversal(node):
    if node is None:
        return     
    in_order_traversal(node.left)
    print(node, end =" ")
    in_order_traversal(node.right)     

def post_order_traversal(node):
    if node is None:
        return   
    post_order_traversal(node.left)
    post_order_traversal(node.right)   
    print(node, end =" ")

    

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
    print("Pre-order:", end =" ")
    pre_order_traversal(A)
    print()

    print("In-order:", end =" ")
    in_order_traversal(A)
    print()

    print("Post-order:", end =" ")
    post_order_traversal(A)
    print()

main() 

        