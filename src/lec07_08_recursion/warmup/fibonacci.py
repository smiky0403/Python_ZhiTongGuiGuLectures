def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    n = 20
    for i in range(n+1):
        res = fibonacci(i)
        print(f"fibonacci for {i} is {res}")

main()
    
    