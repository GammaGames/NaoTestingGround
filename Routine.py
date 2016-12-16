# ****************************************************************
# PROJECT: ShowRobbieGUI
#
# EXECUTION ENVIRONMENTS:
# Python 2.7 on Windows 10,
# Python 2.7 on Windows 7
#
# DEVELOPED WITH:
# Eclipse Neon.1 with PyDev on Windows 10,
# PyCharm Community 2016.3.1 on Windows 7
#
# AUTHORS: Jesse Lieberg, Logan Warner
#
# DESCRIPTION: Routine superclass for routines to run from the GUI
# ****************************************************************

# --------------
# Python imports
# --------------
import sys

# -------------------
# Application imports
# -------------------
from abc import ABCMeta, abstractmethod

class Routine(object):
    '''
    
    '''
    __metaclass__ = ABCMeta

    progressVar = None

    numberSteps = -1
    currentStep = 0
    running = False

    firstFrame = None
    def __init__(self):
        '''
        Default constructor
        '''
    #def __init__

    @abstractmethod
    def connect(self, ip, port):
        return
    #def connect

    @abstractmethod
    def perform(self):
        return
    #perform

    def run(self):
        self.running = True
        try:
            with SetTrace(self.monitor):
                self.perform()
            print self.currentStep
        except StopIteration:
            pass
        finally:
            self.running = False
    #def run
    
    def stop(self):
        self.running = False
    #def stop
    
    def getPercent(self):
        return self.currentStep / float(self.numberSteps) * 100
    #def getPercent

    def monitor(self, frame, event, arg):
        if event == "line":
            if not self.firstFrame:
                self.firstFrame = frame
            if frame == self.firstFrame:
                if not self.running:
                    raise StopIteration
                self.currentStep += 1
        return self.monitor
    #monitor
#class Routine

class SetTrace(object):
    def __init__(self, func):
        self.func = func
    #__init__

    def __enter__(self):
        sys.settrace(self.func)
        return self
    #__enter__

    def __exit__(self, ext_type, exc_value, traceback):
        sys.settrace(None)
    #__exit__
#class SetTrace

#end Routine.py
