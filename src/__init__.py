# -*- coding: utf-8 -*-
'''
Created on 2014-12-25
@summary: Interleaving and random padding random number TEA 
          use c and cython or pure python
@author: fiefdx

Modified on 2014-12-26
@summary: Add 32 and 64 iterations support
@author: fiefdx
'''
import logging

LOG = logging.getLogger(__name__)

WITH_CTEA = False
try:
    import strtea
    import pyctea
    WITH_CTEA = True
except ImportError:
    pass

import pytea

__version__ = "1.0.1"

if WITH_CTEA:
    EncryptStr = pyctea.tea_str_c_encrypt
    DecryptStr = pyctea.tea_str_c_decrypt
else:
    EncryptStr = pytea.str_encrypt
    DecryptStr = pytea.str_decrypt