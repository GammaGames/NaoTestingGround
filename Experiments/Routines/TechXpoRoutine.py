# *************************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS: Python 2.7 on Windows 10
#
# DEVELOPED WITH:
# Eclipse Neon.1 with PyDev on Windows 10,
# PyCharm Community 2016.3 on Windows 7
#
# AUTHORS: Jesse Lieberg, Logan Warner
#
# DESCRIPTION: Demo for TechXpo 2017
# **************************************************************

# --------------
# Python imports
# --------------
import time

# -------------------
# Application imports
# -------------------
import Routine
from naoqi import ALProxy
from CustomMotions import CustomMotions


class TechXpoRoutine(Routine.Routine):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 4
    #def __init__

    def connect(self, IP_PR="10.0.0.7", port_PR=9559):
        self.speechProxy = ALProxy("ALTextToSpeech", IP_PR, port_PR)
        self.autonomousLifeProxy = ALProxy("ALAutonomousLife", IP_PR, port_PR)
        self.motions = CustomMotions(IP_PR, port_PR) # IP and port overridden in case they change
    #def connect

    def run(self):
        self.running = True

        if not self.running:
            return
        
        self.currentStep = 0
        try:
            self.autonomousLifeProxy.setState("solitary")
        except Exception, e:
            # Intentionally left empty to let the routine run on an
            # emulated NAO bot through Choreographe
            pass
        self.motions.standUp()

        self.currentStep = 1
        self.motions.wave(async=True)
        self.speechProxy.say("Hi there, I'm Robbie. I was built by the Aldebaran company in France.")
        self.speechProxy.say("I am the property of the Montana Tech Computer Science Department.")
            
        if not self.running:
            return
        
        self.currentStep = 2
        self.speechProxy.say("This demonstration is a much shorter version"\
                             " of a performance for tours for prospective"\
                             " students.")
        time.sleep(.5)
        self.speechProxy.say("The performance is programmed"\
                             " by the 2016-17 senior software engineering"\
                             " design project team, consisting of"\
                             " Jesse Lieberg and Logan Warner.")
        time.sleep(.5)
        self.speechProxy.say("One of them can show you some pictures of"\
                             "it after I sit back down. I hope you enjoy"\
                             " this year's Tekxpo,"\
                             " thank you for listening.")
        
        if not self.running:
            return
        
        self.currentStep = 3
        self.motions.sitDown()
        try:
            self.autonomousLifeProxy.setState("disabled")
        except Exception, e:
            # Intentionally left empty to let the routine run on an
            # emulated NAO bot through Choreographe 
            pass
    
        if not self.running:
            return
        
        self.currentStep = 4
        self.running = False
    #def run

#end TechXpoRoutine.py
