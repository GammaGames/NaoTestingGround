# ****************************************************************
# PROJECT: ShowRobbieGUI
#
# EXECUTION ENVIRONMENTS: Eclipse Neon.1 with PyDev
#
# DEVELOPED WITH: Python 2.7 on Windows 10
#
# AUTHOR: Jesse Lieberg
#
# DESCRIPTION: Routine superclass for routines to run from the GUI
# ****************************************************************

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
    def run(self):
        return
    #def run
    
    def stop(self):
        self.running = False
    #def stop
    
    def getPercent(self):
        return self.currentStep / float(self.numberSteps) * 100
    #def getPercent
    
#class Routine