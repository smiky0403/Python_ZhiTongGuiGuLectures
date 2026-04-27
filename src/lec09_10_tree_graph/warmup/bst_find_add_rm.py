class Node:
    def __init__ (self, val, left = None, right = None):
        self.val = val
        self.left =left
        self.right = right
    def __repr__ (self):
        return str(self.val)

def find(root, val):
    while root:
        if root.val == val:
            return True
        if root.val > val:
            root = root.left
        else:
            root = root.right
    return False

def add(root, val):
    if not root:
        root = Node(val)
        return True
    
    while root:
        if root.val == val:
            return False
        
        if root.val > val:
            if root.left:
                root = root.left
            else:
                root.left = Node(val)
                print(f"added {val} to left of node {root}")
                return True
        else:
            if root.right:
                root = root.right
            else:
                root.right = Node(val)
                print(f"added {val} to right of node {root}")
                return True            

def remove(root, val):
    if not root: 
        return root

    parent = None
    cur = root
    
    while(cur and cur.val != val):
        parent = cur
        if cur.val > val:
            cur = cur.left
        else:
            cur = cur.right
    
    if not cur:
        return root
    # now we reach the node to be delete and has its parent 
    
    # 1) has both child
    if cur.right and cur.left:
        parent_succ = cur
        succ = cur.right
        
        while succ.left:
            parent_succ = succ
            succ = succ.left
        
        cur.val = succ.val
        
        parent = parent_succ
        cur = succ
    
    # 2) has only 1 kid or no kids
    child = cur.left if cur.left else cur.right    #kid = left or right or None - under node to be delete
    
    if not parent:   #root has the val = key, and root has only 1 child or zero
        return child
    
    if parent.left == cur:
        parent.left = child
    else:
        parent.right = child
    
    return root
    
            
    
    

    

def main():
    # 第一层
    n30 = Node(30)

    # 第二层
    n18 = Node(18); n34 = Node(34); n30.left = n18; n30.right = n34

    # 第三层
    n13 = Node(13); n24 = Node(24); n31 = Node(31); n40 = Node(40)
    n18.left = n13; n18.right = n24; n34.left = n31; n34.right = n40

    # 第四层
    n22 = Node(22); n27 = Node(27); n47 = Node(47)
    n24.left = n22; n24.right = n27; n40.right = n47
    
    print(find(n30, 22))
    print(add(n30, 42))
    
    
main()