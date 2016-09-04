Tea Version 1.0.1
=================
Package functions:
------------------
1. encrypt & decrypt string with interleaving and random padding random number TEA;
2. encrypt & decrypt string with 32 or 64 iterations TEA;

Package features:
-----------------
1. include a pure python encrypt & decrypt module pytea;
2. include a c extension cython encrypt & decrypt module pyctea;
3. pyctea has compatibility with pytea;

Installation
============
1. if you have install numpy and cython at your computer, then run
   cd /path to tea package/
   sudo python ./setup.py install
   you will be install tea with c extension(default use pyctea);
2. if you have not install numpy or cython at your computer, then run
   cd /path to tea package/
   sudo python ./setup.py install
   you will be install tea without c extension(default use pytea);

Help
====
1. you can get examples at /tea-*.*.*/examples/*.py, see & run examples, you can known how to use it;
2. you can get test at /tea-*.*.*/test/*.py, run test scripts, you can known it's performance;
