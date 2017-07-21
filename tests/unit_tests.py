# -*- coding: utf-8 -*-
import unittest
import datetime
import time
import os
import sys
BASEDIR = os.path.abspath(os.path.join(
                          os.path.dirname(os.path.abspath(__file__)),
                          ".."))
sys.path.insert(0, BASEDIR)
import generator

class TestGenerate(unittest.TestCase):
    def test_generate(self):
        result = generator.generate()
        self.assertEqual(result, "password")
        self.assertIsInstance(result, str, "The return type is not a string.")


if __name__ == "__main__":
    unittest.main()
