#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#

# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1、循环
        # if n <= 0: return False
        # while n & 1 == 0:
        #     n = n >> 1
        # return n == 1

        # 2、2的幂的二进制表示只含有一个1
        # return n > 0 and n & (-n) == n
        return n > 0 and n & (n - 1) == 0
# @lc code=end

