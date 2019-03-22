"""
Simulation: Printing Tasks
As students send printing tasks to the shared printer, the tasks are placed in a queue to be processed in a first-come first-served manner.
The most important of these might be whether the printer is capable of handling a certain amount of work. 
If it cannot, students will be waiting too long for printing and may miss their next class.
"""

import random


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

        

"""
The Printer class will need to track whether it has a current task. 
If it does, then it is busy (def busy(self)) and the amount of time needed can be computed from the number of pages in the task. 
The constructor will also allow the pages-per-minute setting to be initialized. 
The tick method decrements the internal timer and sets the printer to idle (self.currentTask = None) if the task is completed.

"""
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate


"""
The Task class will represent a single printing task. 
When the task is created, a random number generator will provide a length from 1 to 20 pages. 
We have chosen to use the randrange function from the random module.
Each task will also need to keep a timestamp to be used for computing waiting time. 
This timestamp will represent the time that the task was created and placed in the printer queue. 
The waitTime method can then be used to retrieve the amount of time spent in the queue before printing begins.

"""
class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

"""The main simulation
The printQueue object is an instance of our existing queue ADT. 
A boolean helper function, newPrintTask, decides whether a new printing task has been created. 
We have again chosen to use the randrange function from the random module to return a random integer between 1 and 180. 
Print tasks arrive once every 180 seconds. 
By arbitrarily choosing 180 from the range of random integers, we can simulate this random event. 
The simulation function allows us to set the total time and the pages per minute for the printer.

"""


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))



def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

"""
Run the simulation for a period of 60 minutes (3,600 seconds) using a page rate of five pages per minute for 10 independent trials.
"""
for i in range(10):
    simulation(3600,5)

