"""
Two-Elevator-Simulation
from EPR-Job No.4
"""
from userinterface import visualize
import random
__author__ = "6598273: Markus Kalusche, 6768647: Tobias Denzer"  # your data
__copyright__ = "Copyright 2017/2018 – Tobias Denzer & Markus Kalusche \
                @ EPR-Goethe-Uni"
__credits__ = "nobody"
__email__ = "s1539940@stud.uni-frankfurt.de"

class Lift():
    """Class Lift"""
    def __init__(self, jobs = [], pos = 0, tick = 0, way = 's'):
        """Constructor"""
        self.jobs = jobs
        self.pos = pos
        self.tick = tick
        self.way = way
    def countjobs(self):
        """Returns an Integer of the Amount of Jobs"""
        return len(self.jobs)
    def getpos(self):
        """Returns an Integer of the Position"""
        return self.pos
    def gettick(self):
        return self.tick
    def getway(self):
        """Returns the Way of the Lift (s/h/r)"""
        return self.way
    def insertjob(self, job):
        """Inserts a new Job to the first Position of the Job-List"""
        if job not in self.jobs:
            self.jobs.insert(0, job)
    def move(self, way):
        """Move the Lift one Tick"""
        if way == 'up':
            self.pos += 1
        if way == 'down':
            self.pos -= 1
        """if self.pos in self.jobs:
            self.jobs.remove(self.pos)"""
        if len(self.jobs) == 0:
            self.way = 's'
    def newjob(self, job):
        """Inserts a new Job to the last Position of the Job-List"""
        if job not in self.jobs:
            self.jobs.append(job)
    def reducetick(self):
        """Reduces the Tick of the Lift by 1"""
        self.tick -= 1
    def settick(self):
        """Set a random Tick for the Lift between 1 and 3"""
        self.tick = random.randint(1, 3)
    def setway(self, way):
        """Set the new Way of the Lift (s/h/r)"""
        self.way = way

def floor_to_index(f, l):
    """Returns the Index as an Integer"""
    if f in l:
        return l.index(f)
    else:
        print(f, 'is not a valid floor! statement skipped.')
        return False

def index_to_floor(i, l):
    """Returns the Floor as a String"""
    return l[int(i)]

def main():
    lift_a = Lift([])
    lift_b = Lift([])
    requests = []
    levels = ['k', 'e', '1', '2', '3', '4']

    while True:
        print('Tick Lift A:', lift_a.gettick())
        print('Tick Lift B:', lift_b.gettick())
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
                        job = floor_to_index(i.replace('a', ''), levels)
                        if job != False:
                            lift_a.newjob(job)
                    elif i.find('b') == 0:
                        job = floor_to_index(i.replace('b', ''), levels)
                        if job != False:
                            lift_b.newjob(job)
                    elif i.find('h') == 1 or i.find('r') == 1:
                        new_req = [floor_to_index(i[0], levels), i[1]]
                        if new_req[0] == 0 and new_req[1] == 'r' \
                            or new_req[0] + 1 == len(levels) and \
                                new_req[1] == 'h':
                                print(i, 'skipped. these buttons do not exist\
                                in that floor!')
                        else:
                            if new_req not in requests:
                                requests.append(new_req)
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
                    lift_b.newjob(requests[0][0])
                    requests.pop(0)

        #moving lift a
        if lift_a.gettick() > 0:
            lift_a.reducetick()
        else:
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
                    lift_a.settick()
                    lift_a.reducetick()

        #moving lift b
        if lift_b.gettick() > 0:
            lift_b.reducetick()
        else:
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
                    lift_b.settick()
                    lift_b.reducetick()

if __name__ == '__main__':
    main()