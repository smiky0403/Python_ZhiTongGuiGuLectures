from typing import List
def search_rotated_arr(arr: List[int], target: int) -> int:
    begin = 0
    final = len(arr) - 1
    
    while(begin <= final):
        mid = (begin + final) // 2
        #print(arr[begin : final + 1])
        #print(mid)
        if arr[mid] == target:
            return mid
        if arr[mid] >= arr[begin]:     #left has order
            if arr[mid] > target >= arr[begin]:
                final = mid - 1
            else:
                begin = mid + 1
        else:                           #right has order
            if arr[mid] < target <= arr[final]:
                begin = mid + 1
            else:
                final = mid - 1
            
            
    return -1
    


def main():
    arr2 = [6,7,0,1,2,3,4,5] #idx: 0 1 2 3 4 5 6 7
    target = 7
    res = search_rotated_arr(arr2, target)
    print(res)
    
main()