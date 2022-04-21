"""Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space."""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ran = len(nums)
        if ran == 0:
            return 1
        
        nums = sorted(nums)
        try:
            ind = nums.index(1)
        except ValueError: 
            return 1
        
        nums = nums[ind:]
        first = 0
        while first < len(nums):
            val = nums[first]
            count = nums.count(val + 1)
            if count == 0:
                return val + 1
            else:
                first += 1
                
               
if __name__ == '__main__':

  #Test:
  nums = [1,2,0]
  out = 3
  #
  Solution_test = Solution()
  test = Solution_test.firstMissingPositive(nums)
  assert test == out
  
