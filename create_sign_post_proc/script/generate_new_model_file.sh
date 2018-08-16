#!/bin/bash 
# -*- coding:utf-8 -*-
##########################################################
# Copyright (c) 2016 Baidu.com, Inc. All Rights Reserved #
##########################################################

"""
use feaset.txt to generate_new_model_file
Filname: generate_new_model_file.sh
Authors: guofangfang02(@baidu.com)
Date: 2016-12-12 11:54:13
"""

## input feaset.txt format is:  fea \t  adfea_sign \t show  \t clk  \t ctr \t weight
## S{ideaid-QueryBigram}:{13248478506-good}:130   10016816113037763347    351 92  0.262108    -0.00265407
feaset_file="./model/feaset.txt.head.utf-8"

new_fea_weight_file="./model/new_fea_weight.txt"

python ./src/map_new_fea_weight.py \
    --input="${feaset_file}" \
    --output="${new_fea_weight_file}"


date_str=`date +%Y%m%d`

final_model='./model/new_model.txt'
mv ${final_model} ${final_model}"."${date_str}

cat ${new_fea_weight_file} | ./create_sign_tool/sign_dsa_title  > ${final_model}
