#!/usr/bin/env python

"""Module contains utility functions for reading CSV files using 
the Python csv library
"""

import csv
import numpy as np

def dict_from_csv(fobj, d={}, delim=' '):
    """Modify a dictionary with data from a CSV file

    where field values can be converted to the float type
    
    Args:
        fobj: file object
        d (dict): reference to a dictionary
        delim (string): delimiter
    """
    reader = csv.reader(fobj)
    line = reader.next() # read 1st line
    keys = line[0].split()

    for k in keys:
        d[k] = []

    for row in reader:
        values = row[0].split()
        for k, v in zip(keys, values):
            d[k].append(float(v))

    # convert to ndarray
    for k in d.keys():
        d[k] = np.asarray(d[k], dtype=float)
    return None

def dict_from_csv2(fobj, d={}, delim=' '):
    """Same as dict_from_csv but without using python's split() function
    """
    reader = csv.reader(fobj, skipinitialspace=True, delimiter=' ')
    keys = reader.next()

    # in case an empty string gets passed to the keys as the last element
    # we get rid of it
    if keys[-1] == '':
        keys = keys[:-1] # what if empty string is not the last?

    for k in keys:
        d[k] = []

    for row in reader:
        for k, v in zip(keys, row):
            d[k].append(float(v))
    return None

def list_from_csv(fobj, labels, delim=' '):
    """Return a list from a CSV file
    
    TODO: elaborate to return a dictionary
    """
    reader = csv.DictReader(fobj, fieldnames=labels, skipinitialspace=True, 
                            delimiter=' ')
    #reader.next()
    csv_list = [(item['TIMEXXX'], item['SX']) for item in reader]
    #for row in reader:
    #    print row['TIMEXXX'] # messed up due to empty space in the file
    return csv_list

if __name__ == '__main__':
    data = {}
    with open('p26_static_n1_e1.dat', 'rb') as f:
        dict_from_csv(f, data)
    print data['TIMEXXX']

    data2 = {}
    with open('p26_static_n1_e1.dat', 'rb') as f:
        dict_from_csv2(f, data2)
    print data2['TIMEXXX']

    with open('p26_static_n1_e1.dat', 'rb') as f:
        data_list = list_from_csv(f, ['TIMEXXX', 'SX'])
    print data_list
