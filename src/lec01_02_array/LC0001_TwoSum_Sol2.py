def two_sum_sol2(arr, target):
    x = dict()
    for i in range(0, len(arr)):
        val = arr[i]
        if( target - val in x):
            print("match")
            return x[target - val], i
        else:
            print("no match")
            x[val] = i
        
    return None, None    
        
    
def main():
    arr = [1,4,20,15,8,6,3]
    a, b = two_sum_sol2(arr, 10)
    print(a, b)
    
main()