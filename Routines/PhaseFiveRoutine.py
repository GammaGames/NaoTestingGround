# *************************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS:
# Python 2.7 on Windows 7
#
# DEVELOPED WITH:
# PyCharm Community 2016.3 on Windows 7
#
# AUTHORS: Logan Warner
#
# DESCRIPTION: Phase 5 of the tour demo
# **************************************************************

# --------------
# Python imports
# --------------
import sys

from CustomMotions import CustomMotions
from naoqi import ALProxy

from NaoTestingGround import Routine


class PhaseFiveRoutine(Routine.Routine):
    '''
    Tour demo phase 5
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 5
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
        self.autonomousLifeProxy.setState("disabled")
        self.running = True

        self.motions.sitDown()
        self.speechProxy.say("I will now return to my post.")

        self.currentStep += 1
        if not self.running:
            return

        self.motions.standUp()
        self.speechProxy.say("Going to stretch my legs a little"\
                             " to get a feel for the carpet")

        self.currentStep += 1
        if not self.running:
            return

        self.motions.turnLeft(.2)
        self.motions.turnRight(.2)

        self.currentStep += 1
        if not self.running:
            return

        self.speechProxy.say("I must now find the mark that marks my post.")
        if not self.motions.lookAroundForMark(68):
            self.fail()

        self.currentStep += 1
        if not self.running:
            return

        self.speechProxy.say("Ah! I see the mark.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(
                68, stoppingDistancePR=.2):
            self.fail()

        self.currentStep += 1
        if not self.running:
            return

        self.motions.turnAround()
        self.motions.sitDown()

        self.running = False
    #run

    def fail(self):
        self.speechProxy.say("I couldn't find the mark.")
        self.motions.sitDown()
        self.running = False
        sys.exit()
    #fail
#end PhaseFiveRoutine.py

demo = PhaseFiveRoutine()
demo.connect()
demo.run()
