#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: svm_process_data.py
#Author: yuxuan
#Created Time: 2016-04-30 19:00:28
############################
def process_data(xfile,yfile,ofile):
    x_file = open(xfile, 'r')
    y_file = open(yfile, 'r')
    output_file = open(ofile, 'w')
    label_y = []
    for i in y_file.readlines():
        label_y.append(float(i.strip())-1.)
    k = 0
    for i in x_file.readlines():
        line = i.strip().split()
        output_file.write(str(label_y[k])+' ')
        k += 1
        for j in range(len(line)):
            output_file.write(str(j+1)+':'+line[j]+' ')
        output_file.write('\n')
    x_file.close()
    y_file.close()
    output_file.close()

process_data('./train/X_train.txt', './train/y_train.txt', 'svm_train.txt')
process_data('./test/X_test.txt', './test/y_test.txt', 'svm_test.txt')
