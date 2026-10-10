class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for a in range(len(nums)):
            if (target-nums[a] not in d):
                d[nums[a]]=a
            else:
                return[a,d[target-nums[a]]]
