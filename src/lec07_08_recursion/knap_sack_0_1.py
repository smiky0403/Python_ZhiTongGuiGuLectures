
from typing import List
def knap_sack_0_1(w: List[int], target: int, idx: int = 0) -> bool:
    if target == 0:
        return True

    if target < 0 or idx >= len(w):
        return False
    
    return knap_sack_0_1(w, target, idx + 1) or knap_sack_0_1(w, target - w[idx], idx + 1)
    
    
def main():
    w= [14, 8, 7, 5, 2]
    target = 20
    print( knap_sack_0_1(w, target))
    
main() 