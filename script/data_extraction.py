# !/usr/bin/env python

"""
________________________________________________________________________________
FILE NAME: data_extraction.py
AUTHOR: Elsior Moreira Alves Junior
PROJECT NAME name: Broker Project
DATE CREATED: 10/28/2019
DATE LAST MODIFIED: 10/28/2019
PYTHON VERSION: 3.7.3
DESCRIPTION: This code bellow was created to automate information extraction
from brokerage pdf files provided by one specific broker in Brazil called CLEAR.
________________________________________________________________________________
"""

# import modules
from tika import parser
import pathlib as pl
from os import chdir


# list of functions
def main():
    """
    Special function to invoke the functions automatically when the program is
    executed.
    """
    extract_pdf()


def extract_pdf():
    """
    A function to extract data from stock market brokerage pdf file
    """
    # ask user input file name
    file_name = input('\n Please, enter file name: ')

    # change to data file path
    path = pl.Path().cwd() / 'data'

    # convert pathlib '/' to windons readble path
    path = str(path)

    # read pdf file
    pdf = parser.from_file(file_name)
    text = pdf['content']
    print(text)

# TODO: multiple file extraction as function argument


if __name__ == '__main__':
    main()
