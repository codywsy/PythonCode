# -*- coding: utf-8 -*-

import unittest
import mathfunc

class TestMathFunc(unittest.TestCase):
    """UnitTest for MatchFunc"""

    def test_add(self):
        """Test method add(a,b)"""
        self.assertEqual(3, mathfunc.add(1,2))
        self.assertNotEqual(3, mathfunc.add(1,1))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, mathfunc.minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, mathfunc.multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, mathfunc.divide(6, 3))
        self.assertEqual(2.5, mathfunc.divide(5, 2))    
    
if __name__ == '__main__':
    unittest.main()