#
# @lc app=leetcode.cn id=917 lang=python
#
# [917] 仅仅反转字母
#

# @lc code=start
class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        l, i, j = list(S), 0, len(S)-1
        while i < j: 
            if l[i].isalpha() and l[j].isalpha(): 
                l[i], l[j] = l[j], l[i]
                i, j = i+1, j-1
                continue
            if not l[i].isalpha(): i += 1
            if not l[j].isalpha(): j -= 1
        return ''.join(l)      
# @lc code=end

