#! /usr/bin/env python3

# Author: David Sosa
# Date: 17.09.2020
# Title: isPermutation.py
# Description: Check if one string is a permutation of the other

import unittest

def is_permutation(stringA, stringB):
  dicA, dicB = {}, {}
  for c in stringA:
    dicA[c] = stringA.count(c)

  for c in stringB:
    dicB[c] = stringA.count(c)

  if dicA==dicB: 
    return True
  else:
    return False

class isPermutationTest(unittest.TestCase):
    def test_isPermutation(self):
          self.assertTrue(is_permutation('abc','cba'))
          self.assertTrue(is_permutation('John','nhoJ'))
          self.assertTrue(is_permutation("aab","aba" ))
          self.assertFalse(is_permutation("aaa","aab"))
          self.assertFalse(is_permutation("aaa","aba" ))

if __name__ == "__main__":
  unittest.main()
