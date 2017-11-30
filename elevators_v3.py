"""
Two-Elevator-Simulation
from EPR-Job No.4
"""
from userinterface import visualize
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"

class Lift():
    def __init__(self, jobs = [], pos = 0, way = 's'):
        self.jobs = jobs
        self.pos = pos
        self.way = way
    def countjobs(self):
        return len(self.jobs)
    def move(self, way):
        if way == 'up':
            self.pos += 1
        if way == 'down':
            self.pos -= 1
        """if self.pos in self.jobs:
            self.jobs.remove(self.pos)"""
        if len(self.jobs) == 0:
            self.status = 's'
    def getpos(self):
        return self.pos
    def getway(self):
        return self.way
    def insertjob(self, job):
        if job not in self.jobs:
            self.jobs.insert(0, job)
    def newjob(self, job):
        if job not in self.jobs:
            self.jobs.append(job)
    def setway(self, way):
        self.way = way

def floor_to_index(f, l):
    return l.index(f)

def index_to_floor(i, l):
    return l[int(i)]

lift_a = Lift([])
lift_b = Lift([])
requests = []
levels = ['k', 'e', '1', '2', '3', '4']

while True:
    print('Requests:', requests)
    print('Jobs Lift A:', lift_a.jobs)
    print('Jobs Lift B:', lift_b.jobs)
    visualize(levels, lift_a, lift_b)

    cin = input('--> ')
    inp = []
    inp = cin.split(' ')

    #statement handler
    if len(cin) > 0:
        for i in inp:
            i = i.lower()
            if len(i) == 2:
                # check if floor is in levels!
                if i.find('a') == 0:
                    lift_a.newjob(floor_to_index(i.replace('a', ''), levels))
                elif i.find('b') == 0:
                    lift_b.newjob(floor_to_index(i.replace('b', ''), levels))
                elif i.find('h') == 1 or i.find('r') == 1:
                    requests.append([floor_to_index(i[0], levels), i[1]])
                else:
                    print(i, 'skipped. please only a,A,b,B,h,H,r,R !')
            else:
                print(i, 'skipped. please only 2 characters per request!')

    #look up requests when lifts are on the ride
    for i in requests:
        if i[1] == 'h':
            if lift_a.getway() == 'h' and lift_b.getway() == 'h' \
            and i[0] >= lift_a.pos and i[0] >= lift_b.getpos():
                if i[0] - lift_a.getpos() < i[0] - lift_b.getpos():
                    lift_a.insertjob(i[0])
                    requests.remove(i)
                    continue
                else:
                    lift_b.insertjob(i[0])
                    requests.remove(i)
                    continue
            else:
                if lift_a.getway() == 'h' and i[0] >= lift_a.getpos():
                    lift_a.insertjob(i[0])
                    requests.remove(i)
                    continue
                if lift_b.getway() == 'h' and i[0] >= lift_b.getpos():
                    lift_b.insertjob(i[0])
                    requests.remove(i)
                    continue
        else:
            if lift_a.getway() == 'r' and lift_b.getway() == 'r' \
            and i[0] <= lift_a.pos and i[0] <= lift_b.getpos():
                if lift_a.getpos() - i[0] < lift_b.getpos() - i[0]:
                    lift_a.insertjob(i[0])
                    requests.remove(i)
                    continue
                else:
                    lift_b.insertjob(i[0])
                    requests.remove(i)
                    continue
            else:
                if lift_a.getway() == 'r' and i[0] <= lift_a.getpos():
                    lift_a.insertjob(i[0])
                    requests.remove(i)
                    continue
                if lift_b.getway() == 'r' and i[0] <= lift_b.getpos():
                    lift_b.insertjob(i[0])
                    requests.remove(i)
                    continue

    #look up if lifts have no jobs anymore
    if len(requests) > 0:
        if lift_a.countjobs() < 1:
            lift_a.newjob(requests[0][0])
            requests.pop(0)
        else:
            if lift_b.countjobs() < 1:
                lift_a.newjob(requests[0][0])
                requests.pop(0)

    #moving lift a
    if lift_a.countjobs() > 0:
        if lift_a.getpos() < lift_a.jobs[0]:
            lift_a.move('up')
            lift_a.setway('h')
        elif lift_a.getpos() > lift_a.jobs[0]:
            lift_a.move('down')
            lift_a.setway('r')
        else:
            lift_a.setway('s')
            lift_a.jobs.pop(0)

    # moving lift b
    if lift_b.countjobs() > 0:
        if lift_b.getpos() < lift_b.jobs[0]:
            lift_b.move('up')
            lift_b.setway('h')
        elif lift_b.getpos() > lift_b.jobs[0]:
            lift_b.move('down')
            lift_b.setway('r')
        else:
            lift_b.setway('s')
            lift_b.jobs.pop(0)