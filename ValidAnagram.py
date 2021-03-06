'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
'''

#Fastest Solution
def isAnagram(self, s: str, t: str) -> bool:   
    #We check for count of characters in both strings and return true if they are equal else false. 
    return all(s.count(x) == t.count(x) for x in 'abcdefghijklmnopqrstuvwxzy') # all function returns True or False depending on values

#Hashmap Approach
# def isAnagram(self, s: str, t: str) -> bool:     
    # count = collections.Counter(s)    #Hashmap for s
    # count2 = collections.Counter(t)   #Hashmap for t
    # if count == count2:               #comparing values for hashmaps
    #     return True
    # return False
    
    
    #Shorter Approach: 
# def isAnagram(self, s: str, t: str) -> bool:     
    # return True if collections.Counter(s) == collections.Counter(t) else False

