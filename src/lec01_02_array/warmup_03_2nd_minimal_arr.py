def second_min(arr):
    if len(arr) < 2:
        return 0

    tmp_min = arr[0]
    tmp_2nd_min = arr[0]
    for i in range(1, len(arr)):
        if arr[i]  < tmp_min:
            tmp_min, tmp_2nd_min = arr[i], tmp_min
        elif arr[i]  < tmp_2nd_min:
            tmp_2nd_min = arr[i]
        print(tmp_min, tmp_2nd_min, sep=" ")
    return tmp_2nd_min

def main():
    arr= [2,-3,4,6,7,-1,10,-20]
    print(second_min(arr))
    
main()