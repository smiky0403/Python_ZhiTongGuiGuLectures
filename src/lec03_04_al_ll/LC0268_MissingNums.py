from typing import List
def missing_nums(nums: List[int]) -> int:
    xor = 0
    
    for i in range(len(nums) + 1):
        xor ^= i
    
    for num in nums:
        xor ^= num
        
    return xor

def main():
    nums = [0, 1, 3]
    result = missing_nums(nums)
    print(result)
 
#xor = 0

#print(3 ^ 2 ^ 1 ^ 0)
#print(7 ^ 6)


 
main()
    