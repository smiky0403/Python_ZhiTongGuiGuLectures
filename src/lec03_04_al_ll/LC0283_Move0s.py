from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) ->None:
        i = j = 0
        while (j < len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            j += 1
            
        while(i < len(nums)):
            nums[i] = 0
            i += 1

def main():
    sol = Solution()
    nums = [1, 2, 0, 3, 0, 5]
    sol.moveZeros(nums)
    print(nums)
    
main()