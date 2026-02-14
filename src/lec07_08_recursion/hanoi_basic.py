def hanoi(n:int, src: str ="A", aux: str = "B", dst: str="C") ->int:
    if n == 0:
        return 0

    moves1 =  hanoi(n-1, src, dst, aux)
    print(f"Move disk{n} from {src} to {dst}")
    moves2 =  hanoi(n-1, aux, src, dst)
    return moves1 + moves2 + 1


def main():
    n = 5
    x= hanoi(5, "X", "Y", "Z")
    print(f"Total moves: {x}")


main()