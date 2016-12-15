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
from multiprocessing import Process

# -------------------
# Application imports
# -------------------
from CustomMotions import CustomMotions
from naoqi import ALProxy
from NaoTestingGround import Routine


class TechXpoRoutine(Routine.Routine, Process):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        Process.__init__(self)
        print "TechXpo routine initializing"
        self.numberSteps = 6
        self.currentStep = 0
    #__init__

    def connect(self, IP_PR, port_PR):
        print "TechXpo routine connecting"
        self.speechProxy = ALProxy("ALTextToSpeech", IP_PR, port_PR)
        self.autonomousLifeProxy = ALProxy("ALAutonomousLife",
                                           IP_PR, port_PR)
        self.motions = CustomMotions(IP_PR, port_PR)
    #connect

    def run(self, IP_PR="10.0.0.7", port_PR=9559):
        print "TechXpo routine running"
        self.running = True
        self.connect(IP_PR, port_PR)

        try:
            self.autonomousLifeProxy.setState("solitary")
        except Exception, e:
            # Intentionally left empty to let the routine run on an
            # emulated NAO bot through Choreographe
            pass
        self.motions.standUp()

        self.currentStep += 1

        self.motions.wave(async=True)
        self.speechProxy.say("Hi there, I'm Robbie. I was built by the Aldebaran company in France.")
        self.speechProxy.say("I am the property of the Montana Tech Computer Science Department.")

        self.currentStep += 1

        self.speechProxy.say("This demonstration is a much shorter version"
                             " of a performance for tours for prospective"
                             " students.")
        time.sleep(.5)

        self.currentStep += 1

        self.speechProxy.say("The performance is programmed"
                             " by the 2016-17 senior software engineering"
                             " design project team, consisting of"
                             " Jesse Lieberg and Logan Warner.")
        time.sleep(.5)

        self.currentStep += 1

        self.speechProxy.say("One of them can show you some pictures of"
                             "it after I sit back down. I hope you enjoy"
                             " this year's Tekxpo,"
                             " thank you for listening.")

        self.currentStep += 1

        self.motions.sitDown()
        try:
            self.autonomousLifeProxy.setState("disabled")
        except Exception, e:
            # Intentionally left empty to let the routine run on an
            # emulated NAO bot through Choreographe 
            pass

        self.currentStep += 1

        self.running = False
    #run

#end TechXpoRoutine.py
