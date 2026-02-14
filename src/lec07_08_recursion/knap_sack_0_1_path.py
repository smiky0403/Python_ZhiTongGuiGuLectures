
from typing import List
def knap_sack_0_1_path(w: List[int], target: int) -> List[List[int]]:
    
    res: List[List[int]] = []
    def dfs(start: int, remain: int, path: List[int]) -> None:
        if remain == 0:
            res.append(path[:])
            return
        if remain < 0 or start >= len(w):
            return

        path.append(w[start])
        dfs(start + 1, remain - w[start], path)
        path.pop()
        
        dfs(start + 1, remain, path)       
    
    dfs(0, target, [])

    return res
    
    
def main():
    w = [14, 8, 7, 5, 2]
    target = 20
    print( knap_sack_0_1_path(w, target))
    
    w0 = []
    w0.append(w[:])   # 拷贝
    w1 = []
    w1.append(w)      # 引用

    # 现在修改原始 w
    w.pop()           # 或 w.append(99)

    print("w  =", w)
    print("w0 =", w0)
    print("w1 =", w1)

    
main() 