========
csv2weka
========

Csv2Weka is a simple analize tool written in python using One Hot Encoding to Label classification

Installation
============

Using git
---------

.. code-block:: bash

    $ git clone https://github.com/rhenter/csv2weka.git
    $ cd csv2weka
    $ python setup.py install

Or, using the Zip file
----------------------

Dowload the file using a web browser

    https://github.com/rhenter/csv2weka/archive/master.zip

Uncompress, go to the folder using a terminal and install as following

.. code-block:: bash

    $ cd csv2weka
    $ python setup.py install

*Add sudo in the beginning if you met problem.


How to use
==========

Help command

.. code-block:: bash

    $ csv2weka --help
    Usage: csv2weka [OPTIONS]

    Python command line tool to prepare CSV files to Weka

    Example:

        $ csv2weka -f capture-sample.csv -o test.arff -h Duration,Protocol,Direction,State,sTos,dTos,TotalPakets,TotalBytes,SourceBytes,Label -c Protocol,State,Direction

    Options:
    -f TEXT    CSV File Name to generate DataFrame.
    -o TEXT    ARFF file Name to use on Weka.
    -c TEXT    Columns to OneHotEncoding.
    -h TEXT    CSV Header fieldnames.
    --version  Show the version and exit.
    --help     Show this message and exit.
