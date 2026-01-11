def findMaxLen(nums:list) -> int:
    cum_sum = 0
    records = {0:-1}  #first index
    res = 0
    
    for i, num in enumerate(nums):
        cum_sum += 1 if num == 1 else -1
        if cum_sum in records:
           res = max(res, i - records[cum_sum])
        else:
            records[cum_sum] = i 
    
    return res
    
    

def main():
    nums = [0,1,1,1,1,1,0,0,0]
    x = findMaxLen(nums)
    print(x)
    

main()