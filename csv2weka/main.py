#!/usr/bin/env python
# encoding: utf-8
import os
import click
import sys

from . import Csv2Weka, __version__


CSV_NAME = 'capture-sample.csv'
ARFF_NAME = 'analized.arff'


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return

    click.echo('translate, version {}'.format(__version__))
    ctx.exit()


@click.command()
@click.option(
    'input_filename', '-f',
    default=CSV_NAME,
    prompt='CSV file Name',
)
@click.option(
    'output_filename', '-o',
    default=ARFF_NAME,
    prompt='CSV file Name',
)
@click.option(
    'selected_columns', '-c',
    prompt='Selected Columns to OneHotEncoding',
)
@click.option(
    'header_names', '-h',
    prompt='CSV Header fieldnames',
)
@click.option(
    '--version',
    callback=print_version,
    expose_value=False,
    is_flag=True,
    is_eager=True,
    help='Show the version and exit.'
)
def main(input_filename, header_names, output_filename, selected_columns):
    """
    Python command line tool to prepare CSV files to Weka

    \b
    Example:
    \b
    \t $ csv2weka -f capture-sample.csv -o test.arff -h Duration,Protocol,Direction,State,sTos,dTos,TotalPakets,TotalBytes,SourceBytes,Label -c Protocol,State,Direction

    """
    click.echo('-' * 25)

    header_names = header_names.split(',')
    selected_columns = selected_columns.split(',')

    csv2weka = Csv2Weka(input_filename, header_names=header_names)

    # Treinando os dados
    click.echo('\nAnalyzing CSV data file ...')
    click.echo('\nDataFrame Training and Adding One Hot Encoding to selected columns ...')
    one_hot_encoding = csv2weka.generate_one_hot_encoding(columns=selected_columns)

    # Exportando dados para um arquivo ARFF (WEKA)
    click.echo('\nExporting data to ARFF file ...')
    csv2weka.dump(one_hot_encoding, output_filename=output_filename)

    click.echo('\nData exported. Please check with Weka software')

    return one_hot_encoding
