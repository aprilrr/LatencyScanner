# test_latencyscanner.py
"""
Tests for LatencyScanner module.
"""

import unittest
from latencyscanner import LatencyScanner

class TestLatencyScanner(unittest.TestCase):
    """Test cases for LatencyScanner class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LatencyScanner()
        self.assertIsInstance(instance, LatencyScanner)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LatencyScanner()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
