# Original challenge can be found here:
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        for number in nums:
            to_find = target - number
            if to_find in nums[i+1:]:
                return [i, nums.index(to_find, i + 1)]
            i += 1
