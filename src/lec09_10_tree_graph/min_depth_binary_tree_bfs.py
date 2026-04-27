from collections import deque
class Node:
    def __init__ (self, val = " ", left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__ (self):
        return str(self.val)

def min_depth_bfs(node):
    if not node:
        return 0

    q = deque([node])
    res = 0
    while q:
        res += 1
        size = len(q)
        for _ in range(size):
            x = q.popleft()
            if not x.left and not x.right:
                return res
            if x.left:
                q.append(x.left) 
            if x.right:
                q.append(x.right) 

    return res
    
    
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
    print(f"Min Depth is: {min_depth_bfs(A)}")


main()