from typing import List
def max_consec_one(nums:List[int]) ->int:
    i =  max_len = cur_max = 0
    
    while(i < len(nums)):

        if nums[i] == 1:
            cur_max += 1
            max_len = max(max_len, cur_max)
        else:
            cur_max = 0
            
        i += 1
            
                
    return max_len


def main():
    nums = [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0]
    result = max_consec_one(nums)
    print(result)
    
main()
    
    
