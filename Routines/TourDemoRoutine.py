# *************************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS:
# Python 2.7 on Windows 7
#
# DEVELOPED WITH:
# PyCharm Community 2016.3 on Windows 7
# PyCharm Community 2016.3 on Manjaro Linux
#
# AUTHORS: Logan Warner
#
# DESCRIPTION: The full tour demo
# **************************************************************

# --------------
# Python imports
# --------------
import math
import sys
import time

from CustomMotions import CustomMotions
from naoqi import ALProxy

from NaoTestingGround import Routine


class TourDemoRoutine(Routine.Routine):
    '''
    Tour demo, all phases
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 19
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
        self.speechProxy.say("Thank you for waking me,"
                             " I have a job to do.")

        if not self.running:
            return
        self.currentStep += 1

        self.motions.standUp()
        self.speechProxy.say("Going to stretch my legs a little"
                             " to get a feel for the carpet")

        if not self.running:
            return
        self.currentStep += 1

        self.motions.turnLeft(.2)
        self.motions.turnRight(.2)

        self.currentStep += 1

        self.speechProxy.say("I must now find the mark on the railing.")
        if not self.motions.lookAroundForMark(107):
            self.fail()

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("Ah! I see the railing mark.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(
                107, stoppingDistancePR=1):
            self.fail()

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("I'm looking for the mark carried by the"
                             " student guide.")

        if not self.running:
            return
        self.currentStep += 1

        if not self.motions.lookAroundForMark(
                114, maxAttemptsPR=float("inf")):
            self.fail()
        self.speechProxy.say("There's the student guide.")
        time.sleep(0.25)
        self.speechProxy.say("Time to welcome our visitors.")
        self.motions.turnToLookAngle()
        time.sleep(1)

        if not self.running:
            return
        self.currentStep += 1

        self.motions.wave(True)
        self.speechProxy.say("Hello, I'm Robbie. I'm a NAO robot.")
        self.motions.lookForward()
        self.motions.lookUp(-math.pi/7)
        self.speechProxy.say("I was designed and manufactured by the"
                             " Japanese company SoftBank.")
        time.sleep(1)

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("While I came with built-in behaviors,"
                             " there's very little I can do without the"
                             " programs made by the students here at"
                             " Montana Tech; programming me is not easy,"
                             " but these students have been taught to"
                             " deal with complex problems.")
        time.sleep(1)

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("I hope you have a pleasant and"
                             " informative visit here at Montana Tech.")
        time.sleep(1)

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("Now I must return to my post.")
        time.sleep(0.25)
        self.speechProxy.say("Have a nice day.")

        self.motions.lookForward()
        self.motions.turnAround()

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("I'm looking for the mark on the shelves"
                             " to get back into the office.")

        if not self.running:
            return
        self.currentStep += 1

        if not self.motions.lookAroundForMark(64):
            self.fail()

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("Ah! There it is.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(
                64, stoppingDistancePR=.35):
            self.fail()

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("I will now return to my post"
                             " using the mark on the water jug.")

        if not self.running:
            return
        self.currentStep += 1

        if not self.motions.lookAroundForMark(68):
            self.fail()

        if not self.running:
            return
        self.currentStep += 1

        self.speechProxy.say("Ah! I see the mark.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(
                68, stoppingDistancePR=.15):
            self.fail()

        if not self.running:
            return
        self.currentStep += 1

        self.motions.turnAround()

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
#end TourDemoRoutine.py
