def two_sum_sol1(arr, target):
    arr = [(idx, value) for idx, value in enumerate(arr)]
    
    arr.sort(key=lambda x: x[1])
    
    i = 0
    j = len(arr) - 1
    
    while(i < j):
        if arr[i][1] + arr[j][1] > target:
            j -= 1
        elif arr[i][1] + arr[j][1] < target:
            i += 1
        else: 
            return arr[i][0] , arr[j][0]
    
    
    
    return arr
    
def main():
    arr = [1,4,20,15,8,6,3];
    a, b = two_sum_sol1(arr, 10)
    print(a, b)
    
main()