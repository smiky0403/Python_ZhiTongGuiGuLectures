def min_arr(arr):
    if len(arr) == 0:
        raise ValueError("empty array")
    if len(arr) < 2:
        return arr[0]
    
    temp = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < temp:
             temp = arr[i]
    return  temp

def main():
    arr = [1,3,-4,6,0]
    print(min_arr(arr))
    
main()