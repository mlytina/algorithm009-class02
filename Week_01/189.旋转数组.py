#
# @lc app=leetcode.cn id=189 lang=python
#
# [189] 旋转数组
#

# @lc code=start
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        #1、暴力法(切片会开辟新的内存,超出时间限制)
        # for i in range(k%len(nums)):
        #     tmp = nums[-1]
        #     nums[1:] = nums[:-1]
        #     nums[0] = tmp
        # return nums

        #类1解法
        # for _ in range(k%len(nums)):
        #     previous = nums[-1]
        #     for i in range(len(nums)):
        #         nums[i], previous = previous, nums[i]

        #2、开新数组
        # k = k%len(nums)
        # if k == 0:
        #     return nums
        # nums[:k], nums[k:] = nums[-k:],nums[:-k]
        # return nums

        #3、前后对掉
        # nums[:] = nums[-k%len(nums):] + nums[:-k%len(nums)]

        #4、插入法(时间过长)
        # k = k % len(nums)
        # for _ in range(k):
        #     nums.insert(0, nums.pop())

        #5、翻转
        # def reserve(num, start, end):
        #     while start < end:
        #         num[start], num[end] = num[end], num[start]
        #         start += 1
        #         end -= 1
        # reserve(nums, 0, len(nums) - 1)
        # reserve(nums, 0, k-1)
        # reserve(nums, k, len(nums) - 1)

        #6、环状替换
        start, count, k = 0, 0, k % len(nums)
        while count < len(nums):
            current = start
            while True:
                next_num = (k + current) % len(nums)
                nums[start], nums[next_num] = nums[next_num], nums[start]
                current = next_num
                count += 1

                if start == current:
                    break
            start += 1



# @lc code=end

