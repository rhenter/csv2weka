#!/usr/bin/env python
# encoding: utf-8
import sys
import os

import arff
import pandas as pd
import click


class Analise:
    def __init__(self, input_filename, header_names=[]):
        self.input_filename = input_filename
        self.output_filename = output_filename
        self.header_names = header_names

    def _create_dataframe(self):
        click.echo('\nAnalyzing CSV data file ...')
        return pd.read_csv(
            self.csv_path, header=None, names=self.header_names, na_values="?", delimiter=';',
            skip_blank_lines=True, skipinitialspace=True
        )

    def dump_to_arff(data_frame, output_filename, relation_name='OneHotEncoding'):
        click.echo('\nExporting data to ARFF file ...')
        return arff.dump(
            output_filename,
            data_frame.values,
            relation=relation_name,
            names=data_frame.columns
        )

    def generate_one_hot_encoding(self, columns=[]):
        click.echo('\nDataFrame Training and Adding One Hot Encoding on the selected columns ...'')
        data_frame = self._create_dataframe()
        return pd.get_dummies(data_frame, columns=columns, dummy_na=False)




if __name__ == '__main__':
    # Variaveis com o nome do arquivo e os campos do arquivo CSV
    csv_name = 'capture-sample.csv'
    header_names = [
        'Duration', 'Protocol', 'Direction', 'State', 'sTos', 'dTos',
        'TotalPakets', 'TotalBytes', 'SourceBytes', 'Label'
    ]

    try:
        csv_name = sys.argv[1]
    except IndexError:
        csv_name = 'capture-sample.csv'
        sys.exit('Match file not found.')

    csv_path = os.path.abspath(csv_name)


    # Criando o DataFrame
    print('Analyzing CSV data file ...')
    data_frame = create_dataframe(csv_name, header_names)

    # Treinando os dados
    print('DataFrame Training and Adding One Hot Encoding to selected columns ...')
    one_hot_encoding = generate_one_hot_encoding(
        data_frame, columns=["Protocol", "Direction", "State"]
    )

    # Exportando dados para um arquivo ARFF (WEKA)
    print('Exporting data to ARFF file ...')
    dump_to_arff(one_hot_encoding)

    print('Data exported. Please check if the arff file wore created.')
