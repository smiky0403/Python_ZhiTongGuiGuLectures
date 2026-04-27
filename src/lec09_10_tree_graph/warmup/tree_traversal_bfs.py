from collections import deque
class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return str(self.val)
    
def bfs_two_queue_traversal(node):
    if node is None:
        return
    q1 = deque([node])
    q2 = deque()
    level = 0
    while q1:
        print(f"level - {level} : ", end =" ")
        level += 1
        while q1:
            x = q1.popleft()
            print(x, end =" ")
            if x.left:
                q2.append(x.left) 
            if x.right:
                q2.append(x.right) 
        q1 = q2
        q2 = deque()
        print()

        

def bfs_null_insertion_traversal(node):
    if node is None:
        return 
    q = deque([node, None])
    level = 0

    while q:
       
        print(f"level - {level} : ", end =" ")
        level += 1
             
        while q[0] is not None:
            x = q.popleft() 
            print(x, end=" ")
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
                
        q.popleft()        
        print()
        if q:
            q.append(None)

def bfs_counting_traversal(node):
    if node is None:
        return 
    q = deque([node])
    level = 0
    while q:
        print(f"level - {level} : ", end =" ")
        level += 1
        size = len(q)
        for i in range(size):
            x = q.popleft()
            print(x, end=" ")
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
        print()
            
    

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
    print("BFS 2 Queue Method:")
    bfs_two_queue_traversal(A)
    print()

    print("BFS Insert None Method")
    bfs_null_insertion_traversal(A)
    print()

    print("BFS Counting Method")
    bfs_counting_traversal(A)
    print()

main() 

        