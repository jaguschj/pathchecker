# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 18:56:54 2020

@author: JensJ
"""
import os
path=os.getenv('path')
print(path)
for p in path.split(';'):
    if os.path.exists(p):
        print('OK',p)
    else:
        print('Error',p)
        