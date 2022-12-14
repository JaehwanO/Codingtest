import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,n in enumerate(nums):
            req = target - n
            if req in nums[i+1:]:
                return [nums.index(n), nums[i+1:].index(req)+(i+1)]