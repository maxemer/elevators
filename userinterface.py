"""
User-interface for Two-Elevator-Simulation
from EPR-Job No.4
"""
#import nothing
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"

def index_to_floor(i, l):
    """Returns the Floor as a String"""
    return l[int(i)]

def list_to_string(j, l):
    """Returns Comma-separated String with Elements of a List"""
    result = ''
    for i in range(len(j)):
        if isinstance(j[i], int):
            result += index_to_floor(j[i], l)
        elif isinstance(j[i], list):
            result += index_to_floor(j[i][0], l) + j[i][1]
        if i + 1 < len(j):
            result += ', '
    return result

def printjobs(l, requests, jobs_a, jobs_b):
    """Print out all Jobs"""
    print('Requests from Floors:', list_to_string(requests, l))
    print('Destinations Lift A:', list_to_string(jobs_a, l))
    print('Destinations Lift B:', list_to_string(jobs_b, l))

def visualize(l, lift_a, lift_b):
    """Print out the Visualization the the Console"""
    i = len(l) - 1
    print('⌈ - A -- -- B - ⌉')
    while i >= 0:
        cout = '⏐ '
        cout += l[i] + ' '
        if lift_a.getpos() == i:
            if lift_a.getway() == 's':
                cout += '[ ]'
            if lift_a.getway() == 'h':
                cout += '/\ '
            if lift_a.getway() == 'r':
                cout += '\/ '
        else:
            cout += '   '
        cout += ' | '
        if lift_b.getpos() == i:
            if lift_b.getway() == 's':
                cout += '[ ]'
            if lift_b.getway() == 'h':
                cout += '/\ '
            if lift_b.getway() == 'r':
                cout += '\/ '
        else:
            cout += '   '
        cout += ' ' + l[i] + ' ⏐'
        print(cout)
        i -= 1
    print('⌊ - A -- -- B - ⌋')