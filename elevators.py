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
    def __init__(self, jobs = [], pos = 0, way = 's',move = 'not'):
        self.jobs = jobs
        self.pos = pos
        self.way = way
        self.move = move
    def getmove(self, move):
        if move == 'up':
            self.pos += 1
        if move == 'down':
            self.pos -= 1
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
    def setway(self, w):
        self.way = w
    def setpos(self, p):
        if p == "up":
            self.pos += 1
        if p == "down":
            self.pos -= 1

def printstats(l, lift_a, lift_b):
    cout = 'A faehrt '
    if lift_a.getway() == 'h':
        cout += 'hoch'
    if lift_a.getway() == 'r':
        cout += 'runter'
    if lift_a.getway() == 's':
        cout = 'A steht'
    print(cout)
    cout = 'B faehrt '
    if lift_b.getway() == 'h':
        cout += 'hoch'
    if lift_b.getway() == 'r':
        cout += 'runter'
    if lift_b.getway() == 's':
        cout = 'B steht'
    print(cout)

#niceigkeit
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

def newrequest(i, l):
    output = []
    if len(i) == 2:
        floor, way = list(i)
        output = [l.index(floor), way]
    return output



lift_a = Lift([])
lift_b = Lift([])
requests = []

levels = ['K', 'E', '1', '2', '3', '4']
# Liste für direction
dir_a = []
dir_b = []

while True:
    req = []
    visualize(levels, lift_a, lift_b)
    cin = input('--> ')
    req = newrequest(cin, levels)
    if len(req) > 0:
        requests.append(req)
        print("success")
        if len(lift_a.getjobs()) <= len(lift_b.getjobs()):
            lift_a.newjob(requests[0])
            requests.pop(0)
            '''
            newlist = lift_a.jobs[0]
            print(newlist)

            
            if lift_a.pos < newlist[0]:
                lift_a.setway("h")
                lift_a.setpos("up")
                print(lift_a.getpos())
            elif lift_a.pos > newlist[0]:
                lift_a.setway("r")
            else:
                lift_a.setway("s")
            '''


            #lift_a.getmove()


        else:
            lift_b.newjob(requests[0])
            requests.pop(0)
            newlist = lift_b.jobs[0]
            print(newlist)
            if lift_b.pos < newlist[0]:
                lift_b.setway("h")
            elif lift_b.pos > newlist[0]:
                lift_b.setway("r")
            else:
                lift_b.setway("s")
           # lift_b.getmove()
    else:
        print("<return> gedrückt")

    if len(lift_a.getjobs()) > 0:
        newlist_a = lift_a.jobs[0]
        print(newlist_a)
        if lift_a.pos < newlist_a[0]:
            lift_a.setway("h")
            lift_a.setpos("up")
            print(lift_a.getpos())
        elif lift_a.pos > newlist_a[0]:
            lift_a.setway("r")
            lift_a.setpos("down")
        else:
            lift_a.setway("s")
            lift_a.jobs.pop(0)
            cabine_input = input("Where to go(A): ")
            if cabine_input != "":
                for i in cabine_input.split(','):
                    tmp = []
                    tmp.append(levels.index(i))
                    lift_a.jobs.insert(0, tmp)
                    print("TEMP=", tmp)

    if len(lift_b.getjobs()) > 0:
        newlist_b = lift_b.jobs[0]
        print(newlist_b)
        if lift_b.pos < newlist_b[0]:
            lift_b.setway("h")
            lift_b.setpos("up")
        elif lift_b.pos > newlist_b[0]:
            lift_b.setway("r")
            lift_b.setpos("down")
        else:
            lift_b.setway("s")
            lift_b.jobs.pop(0)
            cabine_input = input("Where to go(B): ")
            if cabine_input != "":
                for i in cabine_input.split(','):
                    tmp = []
                    tmp.append(levels.index(i))
                    lift_b.jobs.append(tmp)
                    print("TEMP=", tmp)

    print("reg= ", req)
    print("requests=", requests)
    print("lift_a.jobs=",lift_a.jobs )
    print("lift_b.jobs=", lift_b.jobs)





    
