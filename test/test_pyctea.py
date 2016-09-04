# -*- coding: utf-8 -*-
'''
Created on 2014-12-24
@summary: test for pyctea
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
EncryptStr_1 = tea.pyctea.tea_str_c_encrypt
DecryptStr_1 = tea.pyctea.tea_str_c_decrypt
EncryptStr_2 = tea.pyctea.str_c_encrypt
DecryptStr_2 = tea.pyctea.str_c_decrypt

class PycteaTestCase32_1(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr_1
        self.DecryptStr = DecryptStr_1
        self.iterations = 32

class PycteaTestCase64_1(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr_1
        self.DecryptStr = DecryptStr_1
        self.iterations = 64

class PycteaTestCase32_2(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr_2
        self.DecryptStr = DecryptStr_2
        self.iterations = 32

class PycteaTestCase64_2(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr_2
        self.DecryptStr = DecryptStr_2
        self.iterations = 64

if __name__ == "__main__":
    print ">>>>>>>>>>>>>> Function Test Start <<<<<<<<<<<<<<"
    print "EncryptStr 1"
    print "32 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(PycteaTestCase32_1)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print "64 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(PycteaTestCase64_1)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print "EncryptStr 2"
    print "32 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(PycteaTestCase32_2)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print "64 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(PycteaTestCase64_2)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print ">>>>>>>>>>>>>>> Function Test End <<<<<<<<<<<<<<<"
    print ""
    print ">>>>>>>>>>>>> Performance Test Start <<<<<<<<<<<<"
    encrypted_string_en_32 = EncryptStr_1(string_unicode_en, key_unicode, 32)
    encrypted_string_en_64 = EncryptStr_1(string_unicode_en, key_unicode, 64)
    t1 = Timer("EncryptStr_1(string_unicode_en, key_unicode, 32)", 
               "from __main__ import EncryptStr_1, key_unicode, string_unicode_en")
    t2 = Timer("DecryptStr_1(encrypted_string_en_32, key_unicode, 32)", 
               "from __main__ import DecryptStr_1, key_unicode, encrypted_string_en_32")
    print "EncryptStr_1 32 iterations:"
    print "Encrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t1.timeit(test_times))
    print "Decrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t2.timeit(test_times))
    t1 = Timer("EncryptStr_2(string_unicode_en, key_unicode, 32)", 
               "from __main__ import EncryptStr_2, key_unicode, string_unicode_en")
    t2 = Timer("DecryptStr_2(encrypted_string_en_32, key_unicode, 32)", 
               "from __main__ import DecryptStr_2, key_unicode, encrypted_string_en_32")
    print "EncryptStr_2 32 iterations:"
    print "Encrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t1.timeit(test_times))
    print "Decrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t2.timeit(test_times))
    t1 = Timer("EncryptStr_1(string_unicode_en, key_unicode, 64)", 
               "from __main__ import EncryptStr_1, key_unicode, string_unicode_en")
    t2 = Timer("DecryptStr_1(encrypted_string_en_64, key_unicode, 64)", 
               "from __main__ import DecryptStr_1, key_unicode, encrypted_string_en_64")
    print "EncryptStr_1 64 iterations:"
    print "Encrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t1.timeit(test_times))
    print "Decrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t2.timeit(test_times))
    t1 = Timer("EncryptStr_2(string_unicode_en, key_unicode, 64)", 
               "from __main__ import EncryptStr_2, key_unicode, string_unicode_en")
    t2 = Timer("DecryptStr_2(encrypted_string_en_64, key_unicode, 64)", 
               "from __main__ import DecryptStr_2, key_unicode, encrypted_string_en_64")
    print "EncryptStr_2 64 iterations:"
    print "Encrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t1.timeit(test_times))
    print "Decrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t2.timeit(test_times))
    print ">>>>>>>>>>>>>> Performance Test End <<<<<<<<<<<<<"