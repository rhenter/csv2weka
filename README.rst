========
CSV2ARFF
========

CSV2ARFF is a simple analize tool written in python using One Hot Encoding to Label classification

Installation
------------

.. code-block:: bash

   $ cd data_mining
   $ pip install .

Or, using the source and

.. code-block:: bash

   $ python setup.py install

Add sudo in the beginning if you met problem.


How to use
----------

Help command

.. code-block:: bash

    $ csv2weka --help
    Usage: csv2weka [OPTIONS]

    Python command line tool to prepare CSV files to Weka

    Example:

        $ csv2weka -f capture-sample.csv -o test.arff -h Duration,Protocol,Direction,State,sTos,dTos,TotalPakets,TotalBytes,SourceBytes,Label -c Protocol,State,Direction

    Options:
    -f TEXT
    -o TEXT
    -c TEXT
    -h TEXT
    --version  Show the version and exit.
    --help     Show this message and exit.