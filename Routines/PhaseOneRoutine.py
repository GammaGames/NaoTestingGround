# *************************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS:
# Python 2.7 on Windows 10,
# Python 2.7 on Windows 7
#
# DEVELOPED WITH:
# PyCharm Community 2016.3 on Windows 7
# PyCharm Community 2016.3.1 on Windows 7
# GitHub webapp text editor
#
# AUTHORS: Logan Warner
#
# DESCRIPTION: Phase 1 of the tour demo
# **************************************************************

# --------------
# Python imports
# --------------
import sys

from CustomMotions import CustomMotions
from naoqi import ALProxy

from NaoTestingGround import Routine


class PhaseOneRoutine(Routine.Routine):
    '''
    Tour demo phase 1
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 6
        self.currentStep = 0
    # __init__

    def connect(self, IP_PR="10.0.0.7", port_PR=9559):
        self.speechProxy = ALProxy("ALTextToSpeech", IP_PR, port_PR)
        self.autonomousLifeProxy = ALProxy("ALAutonomousLife",
                                           IP_PR, port_PR)
        # IP and port overridden in case they change
        self.motions = CustomMotions(IP_PR, port_PR)
    #connect

    def run(self):
        self.running = True
        self.autonomousLifeProxy.setState("disabled")

        self.motions.sitDown()
        self.speechProxy.say("Thank you for waking me,"\
                             " I have a job to do.")

        if not self.running:
            return
        self.currentStep += 1

        self.motions.standUp()
        self.speechProxy.say("Going to stretch my legs a little"\
                             " to get a feel for the carpet")

        if not self.running:
            return
        self.currentStep += 1

        self.motions.turnLeft(.2)
        self.motions.turnRight(.2)

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("Now I need to find the " \
                             "mark by the doorway.")
        if not self.motions.lookAroundForMark(80):
            self.fail()

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("Ah! I see the doorway mark.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(
                80, stoppingDistancePR=.6):
            self.fail()

        if not self.running:
            return
        self.currentStep += 1

        self.motions.sitDown()

        self.currentStep += 1

        self.running = False
    #run

    def fail(self):
        self.speechProxy.say("I couldn't find the mark.")
        self.motions.sitDown()
        self.running = False
        sys.exit()
    #fail
#end PhaseOneRoutine.py
