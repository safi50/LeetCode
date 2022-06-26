'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
'''

					#---------APPROACH-----------
	'''
	Instead of reversing a linked list physically, think of just reversing the pointers. 
	Example: 
	Given Linked List: 1 -> 2 -> 3 -> 4 -> 5
	Wrong Approach: 5 -> 4 -> 3 -> 2 -> 1 
	CORRECT Approach:  1 <- 2 <- 3 <- 4 <- 5
	VIDEO EXPLANATION: https://www.youtube.com/watch?v=XDO6I8jxHtA
	'''
									#SOLUTION 1: ITERATIVE - FASTEST 
	# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
	        prev, temp = None, head
        while temp:
			#the assingments happen simultaneously when wriiten in a single line, so values are assigned before they are updated
            temp.next, prev, temp = prev, temp, temp.next		#This is an imp line and does not work when writte seperately. Explanation Below:	
        return prev
'''	
			--- EXPLANATION FOR  ---   temp.next, prev, temp = prev, temp, temp.next ---- 
If we have an assignment statement like
l1,l2,l3,l4,... = r1,r2,r3,r4,... ,

Where li are variables and rj may be variables/expressions,

This is how its evaluated:
First values of RHS expressions are stored in temporary variables:
t1 = r1
t2 = r2
t3 = r3
...
And then assigned to LHS variables
l1 = t1
l2 = t2
l3 = t3
...
'''
	
	
	#SOLUTION 2: BASIC AND GOOD -- ITERATIVE
	# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		prev = None
        while head:
            temp = head			 #assign temp to head
            head = head.next		 # head increments
            temp.next = prev #temp still points to head, so temp-> next now points to prev --> for 1st iter, it will be: ( prev <-- temp --> head ....) 
            prev = temp #increment prev to temp 
        return prev
		
		
	#SOLUTION 3: SLOWEST -- RECURSIVE
	# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], prev = None) -> Optional[ListNode]:
        if not head: return prev
        cur, head.next = head.next, prev 		#reverse pointer b/w first two nodes and increment head. after all pointers are changed, return prev
        return self.reverseList(cur, head)
