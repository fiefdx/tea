# -*- coding: utf-8 -*-
'''
Created on 2014-12-25
@summary: test data
@author: fiefdx
'''
from util import md5twice

string_unicode_en = u"This is a test for English string!"
string_unicode_cn = u"这是一个中文测试字符串！"
string_utf_8_en = string_unicode_en.encode("utf-8")
string_utf_8_cn = string_unicode_cn.encode("utf-8")
key_unicode = md5twice(u"testkey")
test_times = 1000