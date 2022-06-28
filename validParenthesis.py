'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[){}"
Output: false

Example 3:
Input: s = "([])"
Output: true
'''

# Implemented using Stack
# If opening and closing tags match, pop from stack , else append. At the end if stack is empty, it means all brackets match so return true.
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = { ')':'(', '}':'{', ']':'['}
        for i in s: 
            if stack and i in dict and stack[-1] == dict[i]:
                stack.pop()
            else: stack.append(i)
        return not stack    # == return not bool(stack) or return true if stack empty & vice versa 
        
        
