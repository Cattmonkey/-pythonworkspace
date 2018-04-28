# -*- coding: utf-8 -*-
"""
Created on  20180427

@author: yyx
"""

'''
将ADPL语法构建成语法矩阵
'''

import sys
import re

print(sys.argv)
matrix = []
with open(sys.argv[1]) as adpl:
	for line in adpl.readlines():
		# matrix.append(re.split(' ', line
		# 	.replace('(', ' ( ')
		# 	.replace(')', ' ) ')
		# 	.replace('\n', '')))
		matrix.append([i for i in line])
print(matrix)
print(matrix[0].index('i'))
print(matrix[1][18])