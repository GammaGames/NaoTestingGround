# *************************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS:
# Python 2.7 on Windows 10,
# Python 2.7 on Windows 7
#
# DEVELOPED WITH:
# Eclipse Neon.1 with PyDev on Windows 10,
# PyCharm Community 2016.3 on Windows 7,
# PyCharm Community 2016.3.1 on Windows 7
#
# AUTHORS: Jesse Lieberg, Logan Warner
#
# DESCRIPTION: Demo for TechXpo 2017
# **************************************************************

# --------------
# Python imports
# --------------
import time

from CustomMotions import CustomMotions
from naoqi import ALProxy

from NaoTestingGround import Routine


class TechXpoRoutine(Routine.Routine):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 14
    #__init__

    def connect(self, IP_PR="10.0.0.7", port_PR=9559):
        self.speechProxy = ALProxy("ALTextToSpeech", IP_PR, port_PR)
        self.autonomousLifeProxy = ALProxy("ALAutonomousLife",
                                           IP_PR, port_PR)
        # IP and port overridden in case they change
        self.motions = CustomMotions(IP_PR, port_PR)
    #connect

    def perform(self):
        try:
            self.autonomousLifeProxy.setState("solitary")
        except Exception, e:
            # Intentionally left empty to let the routine run on an
            # emulated NAO bot through Choreographe
            pass
        self.motions.standUp()

        self.motions.wave(async=True)
        self.speechProxy.say("Hi there, I'm Robbie. I was built by the Aldebaran company in France.")
        self.speechProxy.say("I am the property of the Montana Tech Computer Science Department.")

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

        self.motions.sitDown()
        try:
            self.autonomousLifeProxy.setState("disabled")
        except Exception, e:
            # Intentionally left empty to let the routine run on an
            # emulated NAO bot through Choreographe 
            pass

        self.running = False
    #run

#end TechXpoRoutine.py
