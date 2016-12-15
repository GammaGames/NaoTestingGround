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
# DESCRIPTION: Phase 3 of the tour demo
# **************************************************************

# --------------
# Python imports
# --------------
import sys
import time
import math

# -------------------
# Application imports
# -------------------
import Routine
from naoqi import ALProxy
from CustomMotions import CustomMotions


class PhaseThreeRoutine(Routine.Routine):
    '''
    Tour demo phase 3
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 7
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

        self.currentStep += 1
        if not self.running:
            return

        self.motions.standUp()
        self.speechProxy.say("I'm looking for the student guide"\
                             " carrying mark 114.")

        self.currentStep += 1
        if not self.running:
            return

        if not self.motions.lookAroundForMark(
                114, maxAttemptsPR=float('inf')):
            self.fail()
        self.speechProxy.say("I've seen it. Time to welcome our visitors.")
        time.sleep(1)

        self.currentStep += 1
        if not self.running:
            return

        self.motions.wave(True)
        self.speechProxy.say("Hello, I'm Robbie. I'm a NAO robot."\
                             "I'm designed and manufactured by the"\
                             " Aldebaran company in France, but all"\
                             " of my present behaviors have been"\
                             " programmed as part of a Senior"\
                             " Software Engineering project.")
        time.sleep(1)

        self.currentStep += 1
        if not self.running:
            return

        self.speechProxy.say("There's very little I can do without the"\
                             " programs made by the students here at"\
                             " Montana Tech; programming me is not easy,"\
                             " but these students have been well-equipped"\
                             " by their education here to deal with"\
                             " complex problems.")
        time.sleep(1)

        self.currentStep += 1
        if not self.running:
            return

        self.speechProxy.say("I hope you have a pleasant and "\
                             "informative visit here at Montana Tech.")
        time.sleep(1)

        self.currentStep += 1
        if not self.running:
            return

        self.speechProxy.say("Unfortunately, I can't stay with you longer "\
                             "as I must return to my post. Have a nice day.")

        self.running = False
    #run

    def fail(self):
        self.speechProxy.say("I couldn't find the mark.")
        self.motions.sitDown()
        self.running = False
        sys.exit()
    #fail
#end PhaseThreeRoutine.py

demo = PhaseThreeRoutine()
demo.connect()
demo.run()
