from typing import List

def three_sum_closest(nums: List[int], target: int) -> int:
    nums.sort()
    cur_nearest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        res = target - nums[i]
        j = i + 1
        k = len(nums) - 1
        while(j < k):
            cur_nearest =  update_nearest(cur_nearest, target, nums[i] + nums[j] + nums[k])
            if nums[j] + nums[k] < res:
                j += 1
            elif nums[j] + nums[k] > res:
                k -= 1
            else:
                return target
            
        
    return cur_nearest

def update_nearest(cur_nearest: int, target: int, total: int) -> int:
    if abs(total - target) < abs(cur_nearest - target):
        return total
    else:
        return cur_nearest
    

def main():
    nums = [-1, 2, 1, -4]
    target = 1
    result = three_sum_closest(nums, target)
    print(result)
    
main()