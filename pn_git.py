#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:50:44 2020

@author: ylin
"""

import pandas as pd

if __name__ == '__main__':
    test = pd.read_csv('./Kaggle/Titanic/Data/test.csv')
    train = pd.read_csv('./Kaggle/Titanic/Data/train.csv')
    
    # Now csv files, test and train, have become data frames.  
    print(train.head())
    print(train.tail())
    print(train.describe(include='all'))
    print(train.dtypes)
    print(train.info())
    print(train.columns)
    print(train.columns[3], train.columns[3:5])
    print(train[5:20])
    print(train.shape)
