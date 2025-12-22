from typing import List
def even_odd(arr:List[int]) ->List[int]:
    i, j = 0, len(arr) - 1
    
    while(i < j):
        if(arr[i]%2 == 0 and arr[j]%2 == 1):
            arr[i], arr[j] = arr[j], arr[i]
            i, j = i + 1, j - 1
        elif (arr[i]%2 == 0 and arr[j]%2 == 0):
            j = j - 1
        elif (arr[i]%2 == 1 and arr[j]%2 == 1):
            i = i + 1
        else:
            i, j = i + 1, j - 1
    return arr          
        
def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_arr = even_odd(arr)
    print(arr)

main()