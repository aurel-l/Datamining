Datamining project
==================

Datamining of human protein data

Input file
----------

The input file must be in uniprot-xml format, it can contain any number of proteins.  
The project used a list of all curated human proteins in the uniprot database.  
The path to the file is the first positional argument of the script.

Features
--------

The features available for analysis are:

* `aminoacids`: relative number of each aminoacid in the sequence
* `structure`: relative presence of α-helixes, β-sheets and turns in the sequence
* `phi`: pHI or isoelectric point of the sequence
* `weight`: mean weight of every aminoacid in the sequence
* `length`: length of the sequence

Options
-------

The number of proteins to process can be specified to the script by the `--maximum` option

Usage
-----

Help is available when calling the script with the `-h` options

Requirements
------------

This script is written in python 3

### Dependencies

#### Biopython
the `Bio` module needs to be available in the system or, if not installed, the `Bio` folder needs to be at the project's root.  
http://biopython.org/wiki/Download

#### Numpy
http://www.scipy.org/scipylib/download.html


#### Matplotlib
http://matplotlib.org/downloads.html
