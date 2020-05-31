#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 1、迭代
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        while head and head.next:
            first_node = head
            second_node = head.next

            prev_node.next = second_node
            second_node.next = first_node
            first_node.next = second_node.next
            
            prev_node = head
            head = prev_node.next
        return dummy.next


        # 2、递归
        # if head == None or head.next == None: return head
        # firstnode = head
        # secondnode = head.next
        # firstnode.next = self.swapPairs(secondnode.next)
        # secondnode.next = firstnode

        # return secondnode
# @lc code=end

