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
    'feature_cols', '-f',
    default='',
    prompt='Feature Columns',
    help='Feature Columns to OneHotEncoding.'
)
@click.option(
    'categorical_cols', '-c',
    default='',
    prompt='Categorical Columns',
    help='Columns that are categorical and wont be converted to One Hot Encoded column.'
)
@click.option(
    '--version',
    callback=print_version,
    expose_value=False,
    is_flag=True,
    is_eager=True,
    help='Show the version and exit.'
)
def main(input_filename, output_filename, feature_cols, categorical_cols):
    """
    Python command line tool to convert string data to numerical using
    OneHotEncoding to use on Weka Software

    \b
    Example:
    \b
    \t $ csv2weka -i capture-sample.csv -o test.arff -f Protocol,State,Direction -c Label

    """
    click.echo('-' * 25)

    # Instantiate the Csv2Weka object
    csv2weka = Csv2Weka(input_filename)

    click.echo('\nAnalyzing CSV data file and creating the data frame ...')
    dataframe = csv2weka.create_dataframe()

    if feature_cols:
        feature_cols = feature_cols.split(',')

    if categorical_cols:
        categorical_cols = categorical_cols.split(',')
        dataframe = csv2weka.set_as_category(
            dataframe, categorical_cols
        )

    click.echo('\nDataFrame Training and Adding One Hot Encoding to non numerical columns ...')
    encoded_dataframe = csv2weka.encode(dataframe, feature_cols)

    click.echo('\nExporting data to ARFF file ...')
    output_path = csv2weka.dump(
        data=encoded_dataframe,
        output_filename=output_filename,
        columns=encoded_dataframe.columns
    )

    click.echo(
        '\nData exported on {}. Please check with Weka software'.format(output_path)
    )
