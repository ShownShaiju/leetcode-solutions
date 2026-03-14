# 242. Valid Anagram
# Difficulty: Easy
# Topic: HashMap
# Time: O(n) | Space: O(n)
# https://leetcode.com/problems/valid-anagram/

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s)==Counter(t)
    
# Previous solution
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
#         count = {}
#         for c in s:
#             count[c] = count.get(c, 0) + 1
#         for c in t:
#             if c not in count:
#                 return False
#             count[c] -= 1
#             if count[c] < 0:
#                 return False
#         return True
    

