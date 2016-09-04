# -*- coding: utf-8 -*-
'''
Created on 2014-12-25
@summary: test utils
@author: fiefdx
'''
import hashlib

def md5twice(content):
    '''
    param content must be unicode
    result is unicode
    '''
    m = hashlib.md5(content.encode("utf-8")).hexdigest()
    result = hashlib.md5(m).hexdigest().decode("utf-8")
    return result