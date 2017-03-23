#!/usr/bin/env python
# coding: utf-8
# @File Name: img_gen.py
# @Author: Joshua Liu
# @Email: liuchaozhenyu@gmail.com
# @Create Date: 2017-03-23 16:03:08
# @Last Modified: 2017-03-23 16:03:04
# @Description:

import os

root = './dots'

for fl in os.listdir(root):
    if fl.endswith('.dot'):
        os.system('dot ' + os.path.join(root, fl) + ' -Tsvg -O')
