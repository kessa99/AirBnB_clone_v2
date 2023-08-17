#!/usr/bin/python3

"""
test console
"""

import sys
sys.path.append("..")
import console
import inspect
import pep8
import unittest
HBNBCommand = console.HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Class where test console
    """

    @unittest.skip("Skipping due to FutureWarning")
    def test_conforme_console_of_pep8(self):
        """ test PEP8conform """
        test_pep8 = pep8.StyleGuide(quiet=True)
        r = test_pep8.check_files(['console.py'])
        self.assertEqual(r.total_errors, 0, "Found code style errors.")

    def test_pep8_conforme_test_console(self):
        """ test conforme to PEP8 """
        test_pep8 = pep8.StyleGuide(quiet=True)
        r = test_pep8.check_files(['tests/console.py'])
        self.assertEqual(r.total_errors, 0, "Found code style errors.")
    
    @unittest.skip("Skipping due to FutureWarning")
    def test_console_module_doc(self):
        """ doctrings tests """
        self.assertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand need Doctring for the console")
        self.assertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand needs  doctring")
