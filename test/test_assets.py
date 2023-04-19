import unittest
from unittest import TestCase

from TestingEdge.src.data.assets import get_chr, get_prp, get_env


class TestAssets(TestCase):
    
    def test_get_chr(self):
        self.assertEqual(get_chr(), 'chr')
        
    def test_get_prp(self):
        self.assertEqual(get_prp(), 'prp')

    def test_get_env(self):
        self.assertEqual(get_env(), 'env')
        
        
if __name__ == '__main__':
    unittest.main()