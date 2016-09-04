# -*- coding: utf-8 -*-
'''
Created on 2014-12-24
@summary: test for tea
@author: fiefdx
'''
import os
import sys
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
EncryptStr = tea.EncryptStr
DecryptStr = tea.DecryptStr

class TeaTestCase32(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr
        self.DecryptStr = DecryptStr
        self.iterations = 32

class TeaTestCase64(TempTestCase):
    def setUp(self):
        self.EncryptStr = EncryptStr
        self.DecryptStr = DecryptStr
        self.iterations = 64

if __name__ == "__main__":
    print ">>>>>>>>>>>>>> Function Test Start <<<<<<<<<<<<<<"
    print "32 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(TeaTestCase32)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print "64 iterations:"
    suite = unittest.TestLoader().loadTestsFromTestCase(TeaTestCase64)
    unittest.TextTestRunner(verbosity = 2).run(suite)
    print ">>>>>>>>>>>>>>> Function Test End <<<<<<<<<<<<<<<"
    print ""
    print ">>>>>>>>>>>>> Performance Test Start <<<<<<<<<<<<"
    encrypted_string_en_32 = EncryptStr(string_unicode_en, key_unicode, 32)
    encrypted_string_en_64 = EncryptStr(string_unicode_en, key_unicode, 64)
    t1 = Timer("EncryptStr(string_unicode_en, key_unicode, 32)", 
               "from __main__ import EncryptStr, key_unicode, string_unicode_en")
    t2 = Timer("DecryptStr(encrypted_string_en_32, key_unicode, 32)", 
               "from __main__ import DecryptStr, key_unicode, encrypted_string_en_32")
    print "32 iterations:"
    print "Encrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t1.timeit(test_times))
    print "Decrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t2.timeit(test_times))
    t1 = Timer("EncryptStr(string_unicode_en, key_unicode, 64)", 
               "from __main__ import EncryptStr, key_unicode, string_unicode_en")
    t2 = Timer("DecryptStr(encrypted_string_en_64, key_unicode, 64)", 
               "from __main__ import DecryptStr, key_unicode, encrypted_string_en_64")
    print "64 iterations:"
    print "Encrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t1.timeit(test_times))
    print "Decrypt length(%s) chars string %s times: %s seconds" % (len(string_unicode_en), 
                                                                    test_times, 
                                                                    t2.timeit(test_times))
    print ">>>>>>>>>>>>>> Performance Test End <<<<<<<<<<<<<"