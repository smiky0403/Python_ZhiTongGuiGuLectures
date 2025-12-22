# half-half recursive, (while combine, do it assembly)
def merge_sort(arr):
    
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    
    left_arr = arr[: mid]
    right_arr = arr[mid: ]
    
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    arr = merge(left_arr, right_arr)
    
    return arr
    

    
    
def merge(left_arr, right_arr):
    arr = []
    i = j = 0
    while( i < len(left_arr) and j < len(right_arr) ):
        if left_arr[i] <= right_arr[j]:
            arr.append(left_arr[i])
            i += 1
        else:
            arr.append(right_arr[j])
            j += 1
    
    while( i < len(left_arr) ):
        arr.append(left_arr[i])
        i += 1
        
    while( j < len(right_arr) ):
        arr.append( right_arr[j])
        j += 1    
    
    return arr
    
    
def main():
    arr = [1,6,5,2,7,3,4,8,0]
    arr= merge_sort(arr)
    print(arr)
    print(len(arr)//2)
    #
    
main()