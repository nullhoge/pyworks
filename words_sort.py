#! /usr/bin/env python
# coding: utf-8

import sys

# sysモジュールのsys.argv[0]は実行するプログラム名が
# 入っており、sys.argv[1]からがコマンド引数になる。

input_lists = sys.argv[1:]
input_lists.sort()
print(input_lists)
