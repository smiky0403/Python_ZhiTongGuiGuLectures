def remove_ele(arr, e):
    j = 0
    for i in range (0 , len(arr)):
        if(arr[i] != e):
            arr[j] = arr[i]
            j += 1
        
        

def main():
    arr =[10,9,5,3,9,9,8,6,7,9]
    e = 9
    remove_ele(arr, e)
    print(arr)
    
main()
    