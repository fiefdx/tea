# -*- coding: utf-8 -*-
'''
Created on 2014-12-25
@summary: test lib
@author: fiefdx
'''
import unittest

from data import (string_unicode_en, 
                  string_unicode_cn, 
                  string_utf_8_en, 
                  string_utf_8_cn, 
                  key_unicode, 
                  test_times)

class TempTestCase(unittest.TestCase):
    def setUp(self):
        self.EncryptStr = None
        self.DecryptStr = None
        self.iterations = None

    def test_unicode_en(self):
        print ""
        print "Original unicode String En: ", string_unicode_en
        # input is unicode string or str string
        encrypted_string_en = self.EncryptStr(string_unicode_en, key_unicode, self.iterations)
        # encryped string is str
        self.assertTrue(isinstance(encrypted_string_en, str))
        print "Encrypted String En: ", encrypted_string_en
        decrypted_string_en = self.DecryptStr(encrypted_string_en, key_unicode, self.iterations)
        # decryped string is str
        self.assertTrue(isinstance(decrypted_string_en, str))
        # decryped string == original string
        self.assertTrue(decrypted_string_en.decode() == string_unicode_en)
        print "Decrypted String En: ", decrypted_string_en.decode()

    def test_utf_8_en(self):
        print ""
        print "Original utf-8 String En: ", string_utf_8_en.decode("utf-8")
        # input is unicode string or str string
        encrypted_string_en = self.EncryptStr(string_utf_8_en, key_unicode, self.iterations)
        # encryped string is str
        self.assertTrue(isinstance(encrypted_string_en, str))
        print "Encrypted String En: ", encrypted_string_en
        decrypted_string_en = self.DecryptStr(encrypted_string_en, key_unicode, self.iterations)
        # decryped string is str
        self.assertTrue(isinstance(decrypted_string_en, str))
        # decryped string == original string
        self.assertTrue(decrypted_string_en == string_utf_8_en)
        print "Decrypted String En: ", decrypted_string_en.decode("utf-8")

    def test_unicode_cn(self):
        print ""
        print "Original unicode String Cn: ", string_unicode_cn
        # input is unicode string
        encrypted_string_cn = self.EncryptStr(string_unicode_cn, key_unicode, self.iterations)
        # encryped string is str
        self.assertTrue(isinstance(encrypted_string_cn, str))
        print "Encrypted String Cn: ", encrypted_string_cn
        decrypted_string_cn = self.DecryptStr(encrypted_string_cn, key_unicode, self.iterations)
        # decryped string is str
        self.assertTrue(isinstance(decrypted_string_cn, str))
        # decryped string == original string
        self.assertTrue(decrypted_string_cn.decode("utf-8") == string_unicode_cn)
        print "Decrypted String Cn: ", decrypted_string_cn.decode("utf-8")

    def test_utf_8_cn(self):
        print ""
        print "Original utf-8 String Cn: ", string_utf_8_cn.decode("utf-8")
        # input is unicode string
        encrypted_string_cn = self.EncryptStr(string_utf_8_cn, key_unicode, self.iterations)
        # encryped string is str
        self.assertTrue(isinstance(encrypted_string_cn, str))
        print "Encrypted String Cn: ", encrypted_string_cn
        decrypted_string_cn = self.DecryptStr(encrypted_string_cn, key_unicode, self.iterations)
        # decryped string is str
        self.assertTrue(isinstance(decrypted_string_cn, str))
        # decryped string == original string
        self.assertTrue(decrypted_string_cn == string_utf_8_cn)
        print "Decrypted String Cn: ", decrypted_string_cn.decode("utf-8")