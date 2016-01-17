#! /usr/bin/env python
# coding: utf-8
import sys

try:
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    print(a + b)
except:
    print('error!')
