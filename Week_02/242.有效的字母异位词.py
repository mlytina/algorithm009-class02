#
# @lc app=leetcode.cn id=242 lang=python
#
# [242] 有效的字母异位词
#

# @lc code=start
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # 1、暴力 sort
        # return sorted(s) == sorted(t)

        # 2、26位计数器 若小于0包含不存在的字母 返回false
        # if len(s) != len(t):
        #     return False
        # dic = [0] * 26
        # for i in s:
        #     dic[ord(i)-ord('a')] += 1

        # for j in t:
        #     dic[ord(j) - ord('a')] -= 1
        #     if dic[ord(j) - ord('a')] < 0:
        #         return False
        # return True

        # 3、哈希表
        if len(s) != len(t):
            return False
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        for j in t:
            if j in dic:
                dic[j] -= 1
            else:
                return False

        for val in dic.values():
            if val != 0:
                return False
        return True



# @lc code=end

