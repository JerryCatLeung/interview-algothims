'''Description
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Have you met this question in a real interview? 
Example
Challenge 
O(n3) time
'''
class Solution:
    # @param {string} s1 A string
    # @param {string} s2 Another string
    # @return {boolean} whether s2 is a scrambled string of s1
    def isScramble(self, s1, s2):
        # Write your code here
        if len(s1) != len(s2): 
            return False
        if s1 == s2: 
            return True
        if sorted(s1) != sorted(s2): 
            return False
        
        length=len(s1)
        # find a pos i to split given string to two sections
        for i in range(1,length):
            if self.isScramble(s1[:i],s2[:i]) and self.isScramble(s1[i:],s2[i:]): return True
            #"abcd", "badc"
            # if self.isScramble(s1[:i],s2[length-i:]) and self.isScramble(s1[i:],s2[:length-i]): 
            #     return True
        
        return False
'''Summary
使用递归的思路求解

check below java solutions
https://www.jiuzhang.com/solutions/scramble-string/
'''