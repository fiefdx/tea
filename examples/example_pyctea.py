# -*- coding: utf-8 -*-
'''
Created on 2014-12-25
@summary: example for pyctea
@author: fiefdx
'''
import os
import sys

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

if __name__ == "__main__":
    print ">>>>>>>>>>>>>>>> Examples Start <<<<<<<<<<<<<<<<<"
    print ">>>>>>>>>>>>>>>>> EncryptStr 1 <<<<<<<<<<<<<<<<<<"
    print "Original unicode String En: ", string_unicode_en
    encrypted_string_en = EncryptStr_1(string_unicode_en, key_unicode) # is str
    print "Encrypted string is str instance: ", isinstance(encrypted_string_en, str)
    print "Encrypted String En: ", encrypted_string_en
    decrypted_string_en = DecryptStr_1(encrypted_string_en, key_unicode) # is str
    print "Decrypted string is str instance: ", isinstance(decrypted_string_en, str)
    print "Decrypted String En: ", decrypted_string_en
    print ""
    print "Original utf-8 String En: ", string_utf_8_en
    encrypted_string_en = EncryptStr_1(string_utf_8_en, key_unicode) # is str
    print "Encrypted string is str instance: ", isinstance(encrypted_string_en, str)
    print "Encrypted String En: ", encrypted_string_en
    decrypted_string_en = DecryptStr_1(encrypted_string_en, key_unicode) # is str
    print "Decrypted string is str instance: ", isinstance(decrypted_string_en, str)
    print "Decrypted String En: ", decrypted_string_en
    print ""
    print "Original unicode String Cn: ", string_unicode_cn
    encrypted_string_cn = EncryptStr_1(string_unicode_cn, key_unicode) # is str
    print "Encrypted string is str instance: ", isinstance(encrypted_string_cn, str)
    print "Encrypted String Cn: ", encrypted_string_cn
    decrypted_string_cn = DecryptStr_1(encrypted_string_cn, key_unicode) # is str
    print "Decrypted string is str instance: ", isinstance(decrypted_string_cn, str)
    print "Decrypted String Cn: ", decrypted_string_cn.decode("utf-8")
    print ""
    print "Original utf-8 String Cn: ", string_utf_8_cn.decode("utf-8")
    encrypted_string_cn = EncryptStr_1(string_utf_8_cn, key_unicode) # is str
    print "Encrypted string is str instance: ", isinstance(encrypted_string_cn, str)
    print "Encrypted String Cn: ", encrypted_string_cn
    decrypted_string_cn = DecryptStr_1(encrypted_string_cn, key_unicode) # is str
    print "Decrypted string is str instance: ", isinstance(decrypted_string_cn, str)
    print "Decrypted String Cn: ", decrypted_string_cn.decode("utf-8")
    print ""
    print ">>>>>>>>>>>>>>>>> EncryptStr 2 <<<<<<<<<<<<<<<<<<"
    print "Original unicode String En: ", string_unicode_en
    encrypted_string_en = EncryptStr_2(string_unicode_en, key_unicode) # is str
    print "Encrypted string is str instance: ", isinstance(encrypted_string_en, str)
    print "Encrypted String En: ", encrypted_string_en
    decrypted_string_en = DecryptStr_2(encrypted_string_en, key_unicode) # is str
    print "Decrypted string is str instance: ", isinstance(decrypted_string_en, str)
    print "Decrypted String En: ", decrypted_string_en
    print ""
    print "Original utf-8 String En: ", string_utf_8_en
    encrypted_string_en = EncryptStr_2(string_utf_8_en, key_unicode) # is str
    print "Encrypted string is str instance: ", isinstance(encrypted_string_en, str)
    print "Encrypted String En: ", encrypted_string_en
    decrypted_string_en = DecryptStr_2(encrypted_string_en, key_unicode) # is str
    print "Decrypted string is str instance: ", isinstance(decrypted_string_en, str)
    print "Decrypted String En: ", decrypted_string_en
    print ""
    print "Original unicode String Cn: ", string_unicode_cn
    encrypted_string_cn = EncryptStr_2(string_unicode_cn, key_unicode) # is str
    print "Encrypted string is str instance: ", isinstance(encrypted_string_cn, str)
    print "Encrypted String Cn: ", encrypted_string_cn
    decrypted_string_cn = DecryptStr_2(encrypted_string_cn, key_unicode) # is str
    print "Decrypted string is str instance: ", isinstance(decrypted_string_cn, str)
    print "Decrypted String Cn: ", decrypted_string_cn.decode("utf-8")
    print ""
    print "Original utf-8 String Cn: ", string_utf_8_cn.decode("utf-8")
    encrypted_string_cn = EncryptStr_2(string_utf_8_cn, key_unicode) # is str
    print "Encrypted string is str instance: ", isinstance(encrypted_string_cn, str)
    print "Encrypted String Cn: ", encrypted_string_cn
    decrypted_string_cn = DecryptStr_2(encrypted_string_cn, key_unicode) # is str
    print "Decrypted string is str instance: ", isinstance(decrypted_string_cn, str)
    print "Decrypted String Cn: ", decrypted_string_cn.decode("utf-8")
    print ">>>>>>>>>>>>>>>>> Examples End <<<<<<<<<<<<<<<<<<"