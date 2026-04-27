from typing import List
def search_insertion_pos(arr: List[int], target: int) -> int:
    begin = 0
    final = len(arr) - 1
    
    while(begin <= final):
        mid = (begin + final) // 2
        print(arr[begin : final + 1])
        print(mid)
        
        if arr[mid] == target:
            return mid
        
        if arr[mid] < target:
            begin = mid + 1
        else:
            final = mid - 1
            
    return begin
    


def main():
    arr = [1, 3, 5, 7, 9, 11, 13]  #idx: 0 1 2 3 4 5 6
    arr1 = [1, 3, 5, 7, 9, 11]  #idx: 0 1 2 3 4 5
    res = search_insertion_pos(arr1, 20)
    print(res)
    
main()