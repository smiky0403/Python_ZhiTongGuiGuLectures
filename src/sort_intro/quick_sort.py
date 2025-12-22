# take end of arr as pivot
# i (slower) j (faster) point,  move element j without moving i 
def quick_sort(arr, start, end):
    
    if start >= end:
        return
    
    pivot = arr[end]
    i = start - 1
    for j in range(start, end):
        if(arr[j] < pivot):
            i += 1
            arr[i], arr[j] = arr[j], arr[i] 
    
    i = i + 1
    arr[i], arr[end] = arr[end], arr[i] 
    
    quick_sort(arr, start, i - 1)
    quick_sort(arr, i + 1, end)
    
    return arr


def main():
    arr = [8,2,4,7,1,3,9,6,5]
    quick_sort(arr, 0, len(arr) -1)
    print(arr)
    
main()
    