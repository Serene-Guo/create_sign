#!/usr/bin/env python
# -*- coding:utf-8 -*-
##########################################################
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved #
##########################################################

"""description

Filname: map_new_fea_weight.py
Authors: guofangfang02(@baidu.com)
Date: 2016-12-12 15:38:31
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

def map_new_fea_weight(feaset_file, output_file):
    """docstring for fname"""
    
    if not os.path.exists(feaset_file):
        logging.error("input feaset_file do not exists")
        sys.exit(1)
    
    f_out = open(output_file, "w")

    with open(feaset_file) as f_in:
        for line in f_in:
            line = line.strip()
            line_arr = line.split("\t")
            if len(line_arr) != 6:
                logging.debug("input cols error != 6")
                continue
            fea_txt = line_arr[0]
            weight = line_arr[5]
            ### process fea_txt
            ### S{QueryBigram}:{shenzhen-zhaokao}:32
            fea_txt_arr = fea_txt.split(":")
            new_fea_txt = ":".join(fea_txt_arr[:len(fea_txt_arr)-1])
            
            weight_new_str = weight
            if "e" in weight:
                ## process exp
                weight_f = float(weight)
                weight_new_str = str("%.10f" % weight_f)

            f_out.write("\t".join([new_fea_txt, weight_new_str]) + "\n")


if __name__ == "__main__":
    arg_parser = ArgumentParser(description="description")
    arg_parser.add_argument("-i", "--input", help="input file path")
    arg_parser.add_argument("-o", "--output", dest="output", help="output file path")
    args = arg_parser.parse_args()

    feaset_file = args.input
    output_file = args.output

    map_new_fea_weight(feaset_file, output_file)
    
