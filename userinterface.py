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

def visualize(l, lift_a, lift_b):
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