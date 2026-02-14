from typing import Deque
def climb_building(n:int, memo:dict = None) -> Deque[int]:
    if n < 3:
        return n
        
    a, b = 1, 2
    

    
    for _ in range(3, n + 1):
        a, b = b, a + b
        
    return b

def main():
    n = 15
    res = climb_building(n)
    print(f"climb {n} steps has {res} methods")
    
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