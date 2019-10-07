'''Mapper'''
import sys


for i in sys.stdin:
    ''' Recieve the values from the system input and loop through while
        appending a count of 1 to each'''
    for digit in i:
        print(f'{digit.strip()}''\t', 1)
