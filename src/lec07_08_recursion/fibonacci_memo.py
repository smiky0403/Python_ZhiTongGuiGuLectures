from typing import List
def fibonacci(n: int, memo:List[int] = None) -> int:
    if n == 0 or n == 1:
        return n
    
    if memo is None:
        memo =[0, 1]
    
    if len(memo) > n:
        return memo[n]
    
    memo.append(fibonacci(n - 1, memo) + fibonacci(n - 2, memo))

    return memo[n]

def main():
    n = 20
    memo = [0, 1]
    for i in range(n+1):
        res = fibonacci(i, memo)
        print(f"fibonacci for {i} is {res}")

main()
    
    