#! /usr/bin/env python
# coding: utf-8

import datetime
birthday = datetime.date(1991, 9, 27)
today = datetime.date.today()
diff = today - birthday
print(diff)
