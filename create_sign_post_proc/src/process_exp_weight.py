#!/usr/bin/env python
# -*- coding:gb18030 -*-
##########################################################
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved #
##########################################################

"""description

Filname: process_exp_weight.py
Authors: guofangfang02(@baidu.com)
Date: 2016-12-14 10:37:49
"""

import sys
import os
import traceback
import logging
from argparse import ArgumentParser

logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s %(filename)s[line:%(lineno)d]'
                           ' [%(process)d] %(message)s',
                    datefmt='%m-%d %H:%M:%S',
                    filename=None,
                    filemode='a')

if __name__ == "__main__":
    for line in sys.stdin:
        line = line.strip()
        line_arr = line.split("\t")
        if len(line_arr) < 2:
            continue
        
        fea = line_arr[0]
        weight = line_arr[1]
        
        weight_new = weight
        if "e" in weight:
            weight_f = float(weight)
            weight_new = str("%.8f" % weight_f)
        
        print "\t".join([fea, weight_new])
