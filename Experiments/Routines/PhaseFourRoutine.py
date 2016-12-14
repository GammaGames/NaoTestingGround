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
# DESCRIPTION: Phase 4 of the tour demo
# **************************************************************

# --------------
# Python imports
# --------------
import sys

# -------------------
# Application imports
# -------------------
import Routine
from naoqi import ALProxy
from CustomMotions import CustomMotions


class PhaseFourRoutine(Routine.Routine):
    '''
    Tour demo phase 4
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 5
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
        self.speechProxy.say("I've got to go back now.")

        self.currentStep = 0

        if not self.running:
            return

        self.motions.standUp()
        self.speechProxy.say("Going to stretch my legs a little"\
                             " to get a feel for the carpet")

        self.currentStep = 1

        if not self.running:
            return

        self.motions.turnLeft(.2)
        self.motions.turnRight(.2)

        self.currentStep = 2

        if not self.running:
            return

        self.motions.turnAround()
        self.speechProxy.say("I must now find the mark to get back into the office.")
        if not self.motions.lookAroundForMark(64):
            self.fail()

        self.currentStep = 3

        if not self.running:
            return

        self.speechProxy.say("Ah! I see it.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(64, .2):
            self.fail()

        self.currentStep = 4

        if not self.running:
            return

        self.motions.sitDown()

        self.running = False
    #run

    def fail(self):
        self.speechProxy.say("I couldn't find the mark.")
        self.motions.sitDown()
        self.running = False
        sys.exit()
    #fail
#end PhaseFourRoutine.py

demo = PhaseFourRoutine()
demo.connect()
demo.run()
