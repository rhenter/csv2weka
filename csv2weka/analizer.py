#!/usr/bin/env python
# encoding: utf-8
import os
import sys

import arff
import click
import pandas as pd
from sklearn.preprocessing import OneHotEncoder


class Csv2Weka(object):
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def create_dataframe(self):
        '''
        Create a dataframe using a CSV file
        '''
        return pd.read_csv(
            self.input_filename, header='infer', na_values="?", delimiter=';',
            skip_blank_lines=True, skipinitialspace=True
        )

    def dump(self, data, output_filename, feature_cols, relation_name='OneHotEncoding'):
        '''
        Export data to a ARRF file
        '''
        arff_path = os.path.abspath(output_filename)
        arff.dump(
            output_filename,
            data,
            relation=relation_name,
            names=feature_cols
        )
        return arff_path

    def generate_one_hot_encoding(self, data_frame, feature_cols=[]):
        '''
        Transform all data to numerical usingo OneHotEncoding
        '''
        # One Hot Encoder categorizer
        onehotencoder = OneHotEncoder(categories='auto')

        # if feature_cols:
        #     # Select the data only with the feature cols selected
        #     data_selected = data_frame.loc[:, feature_cols].values
        # else:
        #     # Use all columns
        #     data_selected = data_frame.iloc[:, 0:len(data_frame.columns)].values

        data_selected = data_frame.loc[:, feature_cols].values

        # Convert all String data to a numerical value and convert to a Numpy array
        data_encoded = onehotencoder.fit_transform(data_selected).toarray()

        return data_encoded
