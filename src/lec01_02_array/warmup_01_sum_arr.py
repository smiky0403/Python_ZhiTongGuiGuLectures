import numpy as np

def sum_arr(arr):
    tot = 0
    for i in range(0, len(arr)):
        tot += arr[i]
    return tot

def main():
    arr = [1, 2, 3, 4, 5]
    
    x = sum_arr(arr)
    
    print(x)
    
    x1 = np.array(arr)
    x2 = np.sum(x1)
    x3 = np.sum(x)
    print(x2)
    print(x3)
    
main()
    

    