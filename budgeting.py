#!/usr/bin/env python
import argparse
import csv
from getpass import getpass as getpass

import requests

parser = argparse.ArgumentParser()
parser.add_argument('--url', help='full url from which to download transaction data')
args = parser.parse_args()

user = input('Enter FI user name: ')
pwd = getpass('Enter FI password: ')
auth = (user, pwd)

# get list of potentially new merchants
# download file - may not be able to do this


def get_new_merchants(filename):
    """
    open the file containing potential new merchants

    Note:
        * the file is assumed to be CSV, with fields as follows:
          <TBD>

    :param filename:
    :return:
    """

    with open(filename) as f:

        csv_reader = csv.reader(f)

        for line in csv_reader:

            # PICKUP HERE - remember how to use CSV to read the entries
            # need the field format

# extract merchants
# normalize pot. new merchants (remove chars, spaces, tolower, etc.)
# remove duplicates in a normalized list
# merge pot. new merch w/existing list of merchants

if __name__ == '__main__':

    print(auth)

    if args.url:
        print(args.url)
