#!/usr/bin/env python
# encoding: utf-8
import os
import click
import sys

from . import Csv2Weka, __version__


CSV_NAME = 'capture.csv'
ARFF_NAME = 'oneHotEncoding.arff'


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    click.echo('Csv2Weka, version {}'.format(__version__))
    ctx.exit()


@click.command()
@click.option(
    'input_filename', '-i',
    default=CSV_NAME,
    prompt='CSV file Name',
    help='CSV File Name to generate DataFrame.'
)
@click.option(
    'output_filename', '-o',
    default=ARFF_NAME,
    prompt='ARFF file Name',
    help='ARFF file Name to use on Weka.',
)
@click.option(
    'feature_cols', '-c',
    default='',
    prompt='Feature Columns',
    help='Feature Columns to OneHotEncoding.'
)
@click.option(
    '--version',
    callback=print_version,
    expose_value=False,
    is_flag=True,
    is_eager=True,
    help='Show the version and exit.'
)
def main(input_filename, output_filename, feature_cols):
    """
    Python command line tool to convert string data to numerical using
    OneHotEncoding to use on Weka Software

    \b
    Example:
    \b
    \t $ csv2weka -f capture-sample.csv -o test.arff -c Protocol,State,Direction

    """
    click.echo('-' * 25)

    # Instanciate the Csv2Web object
    csv_path = os.path.abspath(input_filename)
    csv2weka = Csv2Weka(csv_path)

    # Criando o data frame
    click.echo('\nAnalyzing CSV data file and creating the data frame ...')
    data_frame = csv2weka.create_dataframe()

    if not feature_cols:
        feature_cols = data_frame.columns
    else:
        feature_cols = feature_cols.split(',')

    # Convertendo as Strings para valores numericos
    click.echo('\nDataFrame Training and Adding One Hot Encoding to selected columns ...')
    one_hot_encoding = csv2weka.generate_one_hot_encoding(
        data_frame=data_frame,
        feature_cols=feature_cols
    )

    # Exportando dados para um arquivo ARFF (WEKA)
    click.echo('\nExporting data to ARFF file ...')
    output_path = csv2weka.dump(
        data=one_hot_encoding,
        output_filename=output_filename,
        feature_cols=feature_cols
    )

    click.echo(
        '\nData exported on {}. Please check with Weka software'.format(output_path)
    )
