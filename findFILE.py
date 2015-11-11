#!/usr/bin/python



import os, sys
import logging


def loggin():
    # Configure the logging system
    logging.basicConfig(filename='app.log', level=logging.WARNING,
                        format='%(levelname)s:%(asctime)s:%(message)s')

    # Variables (to make the calls that follow work)
    hostname = 'www.python.org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'

    # Example logging calls (insert into your program)
    logging.critical('Host %s unknown', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


def findfile(start, name):
    for relpath, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, relpath, name)
            print(os.path.normpath(os.path.abspath(full_path)))


if __name__ == '__main__':
    loggin()
    findfile(sys.argv[1], sys.argv[2])