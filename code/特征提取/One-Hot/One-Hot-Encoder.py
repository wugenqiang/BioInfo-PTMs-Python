#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@File: One-Hot.py
@Time: 2021/10/29 12:54 下午
@Author: genqiang_wu@163.com
@desc: One-Hot编码实现

"""

'''One-Hot编码实现'''
import pandas as pd
import numpy as np
import re

def one_hot_amino_acid(base_sequence, sequences):
    sequence_to_integer = dict((i, c) for c, i in enumerate(base_sequence))

    one_hot_encoded = []
    for seq in sequences:
        seq = re.sub('-', 'X', seq)
        integer_encoded = [sequence_to_integer[index] for index in seq]
        one_hot_encoded_single = []
        for value in integer_encoded:
            seq = [0 for x in range(len(base_sequence))]
            seq[value] = 1
            # 末尾追加seq
            one_hot_encoded_single.extend(seq)
        one_hot_encoded.append(one_hot_encoded_single)

    return one_hot_encoded

def read_fasta(file):
    with open(file, 'r') as f:
        data = f.readlines()
        print(data)
        sequences = []
        for index, line in enumerate(data):
            # index 从0开始,
            if index % 2 == 0:
                fasta = data[index] + data[index + 1]
                print(fasta)
                # check for and grab sequence name
                if re.search(">", fasta):
                    name = re.split("\n", fasta)[0]
                    sequences.append(re.split("\n", fasta)[1])
                else:
                    name = 'unknown_sequence'
                    sequences.append(fasta)

    f.close()
    return sequences

inputfile = "sample.fasta"
savefile = "sample_one_hot.csv"

base_sequence = 'ACDEFGHIKLMNPQRSTVWYX'

sequences = read_fasta(inputfile)
print(one_hot_amino_acid(base_sequence, sequences))
one_hot = pd.DataFrame(one_hot_amino_acid(base_sequence, sequences))
print(one_hot)
one_hot.to_csv(savefile, index=False, header=False, mode="w+")


