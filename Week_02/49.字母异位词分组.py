#
# @lc app=leetcode.cn id=49 lang=python
#
# [49] 字母异位词分组
#

# @lc code=start
import collections
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # 1、哈希表26位
        # ans = collections.defaultdict(list)
        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1
        #     ans[tuple(count)].append(s)
        # return ans.values()

        # 2、一次循环直接以字母为key
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()

# @lc code=end

