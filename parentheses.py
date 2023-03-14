def parentheses(s):
    while '()' in s or '[]' in s or '{}' in s:
        s = s.replace('()', '').replace('[]', '').replace('{}', '')
    return False if len(s) != 0 else True

'''
https://leetcode.com/problems/valid-parentheses/

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

'''

a = "([)]{}"
print(parentheses(a))
