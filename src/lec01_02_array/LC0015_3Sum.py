def ThreeSum(arr, target):
    
    result = []
    
    arr = [(idx, value) for idx, value in enumerate(arr)]
    arr.sort(key = lambda x:x[1])
    
    if len(arr) < 2:
        return result
    
    for i in range(0, len(arr)):
        delta = arr[i]
        remain = target - delta[1]
        sub_result = TwoSum(arr, remain, i+1)
        for ids in sub_result:
            result.append([delta[0]] + ids)
            
    return result

def TwoSum(arr, target, i):
    
    #i = 0
    j = len(arr) - 1

    result = []
    while(i < j):
        if(arr[i][1] + arr[j][1] > target):
            j -= 1
        elif (arr[i][1] + arr[j][1] < target):
            i += 1
        else:
            result.append([arr[i][0], arr[j][0]] )  
            i += 1
            j -= 1

    return result

def main():
    arr = [-1,0,1,2,-1,-4]
    result = ThreeSum(arr, 0 )
    print(result)
    
main()  