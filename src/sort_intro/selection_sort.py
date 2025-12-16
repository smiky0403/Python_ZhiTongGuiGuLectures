def selection_sort(arr):
    
    if len(arr) < 2:
        return arr
    
    for i in range(0, len(arr) - 1):
        
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[min_idx] > arr[j] :
                min_idx = j
                
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr   



def main():
    arr = [0, 2, 15, 12, 3, 8, 9, 7, 9]
    selection_sort(arr)
    print(arr)


main()