#
# @lc app=leetcode.cn id=191 lang=python
#
# [191] 位1的个数
#

# @lc code=start
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 1、bin + count
        # return bin(n).count('1')
        # 2、for loop
        # n = bin(n)
        # count = 0
        # for c in n:
        #     if c == '1':
        #         count += 1
        # return count
        # 3、位运算
        # count = 0
        # while n:
        #     if n & 1 == 1:
        #         count += 1
        #     n = n >> 1
        # return count
        # count = 0
        # while n:
        #     count += n&1
        #     n = n>>1
        # return count
        # 4、位运算2
        count = 0
        while n != 0:
            count += 1
            n = n & (n - 1)
        return count
        
# @lc code=end

