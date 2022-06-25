'''
Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []
'''
#APPROACH 1: ITERATION
Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head is not None and  head.val == val: head = head.next #If head is same as value, skip head and head becomes head.next
        temp = head
        while temp is not None: 
            if temp.next is not None and temp.next.val == val: #keep checking if temp is None because if it is , next nodes are also None, so ERROR
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head



#APPROACH 1 : RECURSION

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # if head is None: return
        # head.next = self.removeElements(head.next, val)
        # return head.next if head.val == val else head
'''
 It basically goes down to the last null node, and rebuilds the linked list, by adding only the nodes which are not equal to val to this null, 
 For List = [1,2,6,3,4,5,6] ->  it goes from
iter 1:	null ;
iter 2:	[5->null] //when head is 6 it doesnt add anything to head
iter 3:	[4-->5-->null]
iter 4:	[3-->4-->5-->-->null]
iter 5:	[2-->3-->4-->5-->null]
iter 6:	[1-->2-->3-->4-->5-->null]
ANSWER: [1,2,3,4,5]
'''
