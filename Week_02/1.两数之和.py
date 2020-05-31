#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return i,j

        # dic = {}
        # for i, num in enumerate(nums):
        #     if target - num in dic:
        #         return dic[target - num], i
        #     dic[num] = i

        nums = enumerate(nums)
        nums = sorted(nums, key=lambda x:x[1])
        l, r = 0, len(nums)-1
        while l < r:
            if nums[l][1] + nums[r][1] == target:
                return nums[l][0], nums[r][0]
            if nums[l][1] + nums[r][1] < target:
                l += 1
            else:
                r -= 1



        
        
# @lc code=end

