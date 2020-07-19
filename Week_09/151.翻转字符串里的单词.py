#
# @lc app=leetcode.cn id=151 lang=python
#
# [151] 翻转字符串里的单词
#

# @lc code=start
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ': i -= 1
            res.append(s[i + 1: j + 1])
            while s[i] == ' ': i -= 1
            j = i
        return ' '.join(res)
# @lc code=end

