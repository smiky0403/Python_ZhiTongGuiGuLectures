def climb_building(n:int) -> int:
    if n < 3:
        return n
    return climb_building(n - 1) + climb_building(n -2)


def main():
    n = 10
    res = climb_building(n)
    print(f"climb {n} steps has {res} methods")
    
main()