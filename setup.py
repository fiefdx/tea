# -*- coding: utf-8 -*-
'''
Created on 2014-12-26
@summary: Interleaving and random padding random number TEA 
          use c and cython or pure python
@author: fiefdx
'''

from distutils.core import setup
from distutils.extension import Extension

WITH_EXTENSION = False
try:
    from Cython.Distutils import build_ext
    import numpy
    WITH_EXTENSION = True
    print "Install tea with C extension!"
except ImportError:
    print "Warning: Install tea without C extension!"
    print ("If you want install tea with C extension, "
           "please install Numpy and Cython first!")

kwargs = {}
kwargs["name"] = "tea"
kwargs["version"] = "1.0.1"
kwargs["author"] = "fiefdx"
kwargs["author_email"] = "fiefdx@gmail.com"
kwargs["packages"] = ["tea"]
kwargs["package_dir"] = {"tea":"src"}

if WITH_EXTENSION:
    strtea = Extension(
        name = 'strtea',
        sources = ['lib/strctea.pyx', 'lib/strtealink.pxd', 'lib/strtea.c'],
        include_dirs = ['lib', numpy.get_include()]
    )

    kwargs["cmdclass"] = {'build_ext': build_ext}
    kwargs["ext_modules"] = [strtea]
else:
    pass

setup(**kwargs)