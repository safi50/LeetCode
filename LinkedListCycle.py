'''
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
'''

#Solution 1:  Tortoise and Hare Algorithm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head != None and head.next != None:  #check if head and head.next node exists
            slow = head           #define two pointers
            fast = head.next
        try:
            while slow is not fast:     #after some time, the fast pointer eventually catches upto slow and they become equal if cycle exists.
                slow = slow.next        
                fast = fast.next.next
            return True
        except: #if there is no cycle, Fast will reach end of linked list and on next iteration, it will return an error bcz fast.next.next doesnt exist
            return False
          
            #Solution 2: Without Try and Except Block
# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
            # slow = fast = head 
            # while fast and fast.next:
            #     slow = slow.next
            #     fast = fast.next.next
            #     if slow == fast:
            #         return True
            # return False

          
          
          
          
