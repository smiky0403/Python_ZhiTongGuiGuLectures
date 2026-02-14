from typing import List
def climb_building(n:int, memo:dict = None) -> int:
    if n < 3:
        return n
        
    if memo is None:
        memo = {1:1, 2:2}
    
    if n in memo:
        return memo[n]
    #climb_building(n - 1, memo) + climb_building(n -2, memo)
    
    memo[n] = climb_building(n - 1, memo) + climb_building(n - 2, memo)
    return memo[n]


def main():
    n = 6
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