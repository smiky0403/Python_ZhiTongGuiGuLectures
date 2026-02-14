from typing import List, Optional, Dict
def climb_building(n: int , memo: Optional[Dict[int, List[str]]] = None) -> List[str]:

    if memo is None:
        memo = {}  #give an empty dict at begining
    if n == 0:
        return [""]    
    if n == 1:
        return ["1"]
    if n == 2:
        return ["1-1", "2"]
        
    res: List[str] = []
    
    if n in memo:
        return memo[n]
    
    for p in climb_building(n -1, memo):
        res.append( "1" if p == "" else f"1-{p}")
    for p in climb_building(n -2, memo):
        res.append( "2" if p == "" else f"2-{p}")
    
    memo[n] = res
    return res


def main():
    n = 6
    res = climb_building(n)
    print(f"climb {n} steps has {len(res)} methods")
    
    for i, p in enumerate(res):
        print(f"climb {n} steps has method of as: {p}")
    
main()

"""
    climb(6) [*]
├─ climb(5) [*]
│  ├─ climb(4) [*]
│  │  ├─ climb(3) [*]
│  │  │  ├─ climb(2) [B]   -> return 2
│  │  │  └─ climb(1) [B]   -> return 1
│  │  │      => memo[3] = 3
│  │  └─ climb(2) [B]      -> return 2
│  │      => memo[4] = memo[3]+2 = 5
│  └─ climb(3) [M]         -> return memo[3] = 3
│      => memo[5] = memo[4]+memo[3] = 8
└─ climb(4) [M]             -> return memo[4] = 5
    => memo[6] = memo[5]+memo[4] = 13

"""