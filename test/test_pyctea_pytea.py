# -*- coding: utf-8 -*-
'''
Created on 2014-12-26
@summary: test for pyctea's compatibility with pytea
@author: fiefdx
'''
import os
import sys
import hashlib
import timeit
from timeit import Timer
import unittest

from test_lib import TempTestCase
from data import (string_unicode_en, 
                  string_unicode_cn, 
                  string_utf_8_en, 
                  string_utf_8_cn, 
                  key_unicode, 
                  test_times)

import tea
EncryptStr = tea.pytea.str_encrypt
DecryptStr = tea.pytea.str_decrypt
EncryptStr_1 = tea.pyctea.tea_str_c_encrypt
DecryptStr_1 = tea.pyctea.tea_str_c_decrypt
EncryptStr_2 = tea.pyctea.str_c_encrypt
DecryptStr_2 = tea.pyctea.str_c_decrypt

class PycteaPyteaTestCase32_1(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr
        self.DecryptStr = DecryptStr_1
        self.iterations = 32

class PycteaPyteaTestCase64_1(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr
        self.DecryptStr = DecryptStr_1
        self.iterations = 64

class PycteaPyteaTestCase32_2(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr
        self.DecryptStr = DecryptStr_2
        self.iterations = 32

class PycteaPyteaTestCase64_2(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr
        self.DecryptStr = DecryptStr_2
        self.iterations = 64

if __name__ == "__main__":
    print ">>>>>>>>>>>>>> Compatibility Test Start <<<<<<<<<<<<<<"
    print "EncryptStr 1, pytea encrypt, pyctea decrypt"
    print "32 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(PycteaPyteaTestCase32_1)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print "64 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(PycteaPyteaTestCase64_1)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print "EncryptStr 2, pytea encrypt, pyctea decrypt"
    print "32 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(PycteaPyteaTestCase32_2)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print "64 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(PycteaPyteaTestCase64_2)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print ">>>>>>>>>>>>>>> Compatibility Test End <<<<<<<<<<<<<<<"