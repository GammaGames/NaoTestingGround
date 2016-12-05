# *************************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS: Python 2.7 on Windows 10
#
# DEVELOPED WITH: PyCharm Community 2016.3 on Windows 7
#
# AUTHORS: Logan Warner
#
# DESCRIPTION: Phase 1 of the tour demo
# **************************************************************

# --------------
# Python imports
# --------------
import math

# -------------------
# Application imports
# -------------------
import Routine
from naoqi import ALProxy
from CustomMotions import CustomMotions
import NaoMarkModule


class PhaseOneRoutine(Routine.Routine):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 8
    # __init__

    def connect(self, IP_PR="10.0.0.7", port_PR=9559):
        self.speechProxy = ALProxy("ALTextToSpeech", IP_PR, port_PR)
        self.autonomousLifeProxy = ALProxy("ALAutonomousLife", IP_PR, port_PR)
        # IP and port overridden in case they change
        self.motions = CustomMotions(IP_PR, port_PR)
    #connect

    def run(self):
        self.autonomousLifeProxy.setState("disabled")
        self.running = True

        self.motions.sitDown()

        self.currentStep = 0

        if not self.running:
            return

        self.speechProxy.say("Thank you for waking me,"\
                             " I have a job to do.")

        self.currentStep = 1

        if not self.running:
            return

        self.speechProxy.say("The first thing I must do "\
                             "is find the mark by the doorway.")

        self.currentStep = 2

        if not self.running:
            return

        self.motions.lookTo(0, 20)
        markData = self.motions.lookAroundForMark(107)

        self.currentStep = 3

        if not self.running:
            return

        self.speechProxy.say("Ah! I see the doorway mark.")

        self.currentStep = 4

        if not self.running:
            return

        self.motions.standUp()

        self.currentStep = 5

        if not self.running:
            return

        self.speechProxy.say("I will now walk toward it.")

        self.currentStep = 6

        if not self.running:
            return

        x, y, z = NaoMarkModule.getMarkXYZ(self.motions.motionProxy,
                                           markData,
                                           self.motions.naoMarkSize)
        verticalAngle, horizontalAngle = NaoMarkModule.getMarkAngles(markData)
        horizontalAngle = math.degrees(horizontalAngle)
        print "angle is {}".format(horizontalAngle)
        self.motions.walkTo(x - .6, y, horizontalAngle)

        self.currentStep = 7

        if not self.running:
            return

        self.motions.sitDown()

        self.running = False
    #run

#end PhaseOneRoutine.py

demo = PhaseOneRoutine()
demo.connect()
demo.run()