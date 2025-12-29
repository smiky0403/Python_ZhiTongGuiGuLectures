from typing import List, Dict

def reverse_list(arr: List[int] ) -> List[int]:
    i, j = 0, len(arr) - 1
    while(i < j):
        arr[i], arr[j] =  arr[j], arr[i]
        i += 1
        j -= 1
    return arr


def main():
    arr = [1, 2, 3, 4, 5]
    new_arr = reverse_list(arr)
    print(new_arr)
    
main()