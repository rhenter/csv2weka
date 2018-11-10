#!/usr/bin/env python
# encoding: utf-8
import sys
import os

import arff
import pandas as pd
import click


class Csv2Weka:
    def __init__(self, input_filename, header_names=[]):
        self.input_filename = input_filename
        self.header_names = header_names

    def _create_dataframe(self):
        csv_path = os.path.abspath(self.input_filename)
        return pd.read_csv(
            csv_path, header=None, names=self.header_names, na_values="?", delimiter=';',
            skip_blank_lines=True, skipinitialspace=True
        )

    def dump(self, data_frame, output_filename, relation_name='OneHotEncoding'):
        return arff.dump(
            output_filename,
            data_frame.values,
            relation=relation_name,
            names=data_frame.columns
        )

    def generate_one_hot_encoding(self, columns=[]):
        data_frame = self._create_dataframe()
        return pd.get_dummies(data_frame, columns=columns, dummy_na=False)
