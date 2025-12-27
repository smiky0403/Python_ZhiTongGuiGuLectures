from typing import List
def rotary_arr(nums: List[int], k: int) -> None:

    k = k%len(nums)
    reverse_array(nums, 0, len(nums) - 1)
    reverse_array(nums, 0, k - 1)
    reverse_array(nums, k, len(nums) - 1)
    
    
def reverse_array(nums:List[int], i: int, j:int) -> None:
    while(i < j):
        nums[i], nums[j] = nums[j], nums[i]
        i, j = i + 1, j - 1

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8 ,9]
    rotary_arr(arr, 3)
    
    print(arr)
    
main()