#!/usr/bin/env python
# encoding: utf-8
import os
import sys

import arff
import click
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


class Csv2Weka(object):
    def __init__(self, filename, delimiter=','):
        # Check if the file exists before start
        if not os.path.exists(os.path.abspath(filename)):
            exc = '{} not exists'.format(filename)
            raise FileNotFoundError(exc)

        # Set attributes
        self.filename = filename
        self.delimiter = delimiter

    def create_dataframe(self):
        '''
        Create a dataframe from a CSV file
        '''
        dataframe = pd.read_csv(
            self.filename, header='infer', na_filter=False, delimiter=self.delimiter,
            skip_blank_lines=True, skipinitialspace=True, thousands=r'.',
            squeeze=True, verbose=True
        )
        return dataframe

    def set_as_category(self, dataframe, columns):
        '''
        Set a column as categorical
        '''
        for column in columns:
            new_column = getattr(dataframe, column).astype('category')
            setattr(dataframe, column, new_column)
        return dataframe

    def dump(
        self, data, columns, output_filename, relation_name='OneHotEncoding'
    ):
        '''
        Export data to a ARRF file
        '''
        # Dump function for dumping values to a file
        arff_path = os.path.abspath("{}.arff".format(output_filename))

        # TOFIX: Arff lib is changing some feature columns type
        arff.dump(
            arff_path,
            data,
            relation=relation_name,
            names=columns,
        )

        return arff_path

    def encode(self, dataframe, feature_cols=[]):
        '''
        Transform all data to numerical using OneHotEncoding
        '''
        # One Hot Encoder categorizer
        onehotencoder = OneHotEncoder(categories='auto', sparse=False)

        # Select all non numerical columns
        to_encode = feature_cols or dataframe.select_dtypes('object').columns

        # Generate All columns using oneHotEncode
        data_encoded = pd.get_dummies(dataframe, columns=to_encode)

        return data_encoded
