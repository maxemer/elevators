"""
Two-Elevator-Simulation
from EPR-Job No.4
"""
#import nothing
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"

class Lift(object):
    def __init__(self, jobs = [], pos = 0, way = 's'):
        self.jobs = jobs
        self.pos = pos
        self.way = way
    def move(self):
        if self.way == 'r':
            self.pos -= 1
        if self.way == 'h':
            self.pos += 1
        if self.pos in self.jobs:
            self.jobs.remove(self.pos)
    def getjobs(self):
        return self.jobs
    def getpos(self):
        return self.pos
    def getway(self):
        return self.way
    def newjob(self, job):
        if job not in self.jobs:
            self.jobs.append(job)

def visualize(l, lift_a, lift_b):
    i = len(l) - 1
    print('# # A # B # #')
    while i >= 0:
        cout = '# '
        cout += l[i] + ' '
        if lift_a.getpos() == i:
            if lift_a.getway() == 's':
                cout += 'o'
            if lift_a.getway() == 'r':
                cout += 'V'
            if lift_a.getway() == 'h':
                cout += '^'
        else:
            cout += ' '
        cout += ' # '
        if lift_b.getpos() == i:
            if lift_b.getway() == 's':
                cout += 'o'
            if lift_b.getway() == 'r':
                cout += 'V'
            if lift_b.getway() == 'h':
                cout += '^'
        else:
            cout += ' '
        cout += ' ' + l[i] + ' #'
        print(cout)
        i -= 1
    print('# # A # B # #')

def newrequest(i, l):
    output = []
    if len(i) == 2:
        floor, way = list(i)
        output = [l.index(floor), way]
    return output

lift_a = Lift()
lift_b = Lift()
requests = []
levels = ['k', 'e', '1', '2', '3', '4']

visualize(levels, lift_a, lift_b)

while True:
    cin = input('--> ')
    req = newrequest(cin, levels)
    if len(req) > 0:
        requests.append(req)