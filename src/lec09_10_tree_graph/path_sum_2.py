class TreeNode:
    def __init__ (self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


def path_sum_2(root, target_sum):
    
    res = []
    path = []
    def dfs(cur, remain):
        if not cur:
            return
        
        remain -= cur.val
        path.append(cur.val)
        
        if not cur.left and not cur.right:
            if remain == 0:
                res.append(path.copy())
                path.pop()
        else:
            dfs(cur.left, remain)
            dfs(cur.right, remain)  
            path.pop()   
    
    dfs(root, target_sum)
    return res
    
def build_example_tree():
    # level 0
    n5 = TreeNode(5)

    # level 1
    n4_left = TreeNode(4)
    n8 = TreeNode(8)
    n5.left = n4_left
    n5.right = n8

    # level 2
    n11 = TreeNode(11)
    n13 = TreeNode(13)
    n4_right = TreeNode(4)
    n4_left.left = n11
    n8.left = n13
    n8.right = n4_right

    # level 3
    n7 = TreeNode(7)
    n2 = TreeNode(2)
    n1 = TreeNode(1)
    n11.left = n7
    n11.right = n2
    n4_right.right = n1

    return n5

def main():
    root = build_example_tree()
    target_sum = 22
    res = path_sum_2(root, target_sum)
    
    print(res)
    

main()