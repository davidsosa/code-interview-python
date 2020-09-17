#! /usr/bin/env python3

# Author: David Sosa
# Date: 15.09.2020
# Title: isUnique.py
# Description: Determines if a string has all unique characthers

import unittest

def is_unique(my_string):
    seen_char = []
    for c in my_string:
        if c in seen_char:
            return False
        seen_char.append(c)
    return True

class isUniqueTest(unittest.TestCase):
    def test_isUnique(self):
          self.assertFalse(is_unique("aaaaaa"))
          self.assertTrue(is_unique("abcdefg"))
          self.assertFalse(is_unique("!!"), )

if __name__ == "__main__":
  unittest.main()