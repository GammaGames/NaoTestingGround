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
import sys
import time
import math

# -------------------
# Application imports
# -------------------
import Routine
from naoqi import ALProxy
from CustomMotions import CustomMotions


class TourDemoRoutine(Routine.Routine):
    '''
    Tour demo, all phases
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 15
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
        self.speechProxy.say("Thank you for waking me,"
                             " I have a job to do.")

        self.currentStep += 1

        if not self.running:
            return

        self.motions.standUp()
        self.speechProxy.say("Going to stretch my legs a little"
                             " to get a feel for the carpet")

        self.currentStep += 1

        if not self.running:
            return

        self.motions.turnLeft(.2)
        self.motions.turnRight(.2)

        self.currentStep += 1

        self.speechProxy.say("I must now find the mark on the railing.")
        if not self.motions.lookAroundForMark(107):
            self.fail()

        self.currentStep += 1

        if not self.running:
            return

        self.speechProxy.say("Ah! I see the railing mark.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(107, 1):
            self.fail()

        self.currentStep += 1

        if not self.running:
            return


        self.motions.standUp()
        self.speechProxy.say("I'm looking for the mark carried by the"
                             "student guide.")

        self.currentStep += 1

        if not self.running:
            return

        if not self.motions.lookAroundForMark(114):
            self.fail()
        self.speechProxy.say("There's the student guide."
                             "Time to welcome our visitors.")
        self.motions.turnToLookAngle()
        time.sleep(1)

        self.currentStep += 1

        if not self.running:
            return

        self.motions.wave(True)
        self.speechProxy.say("Hello, I'm Robbie. I'm a NAO robot.")
        self.motions.lookForward()
        self.motions.lookUp(-math.pi/7)
        self.speechProxy.say("I was designed and manufactured by the"
                             " Japanese company SoftBank.")
        time.sleep(1)

        self.currentStep += 1

        if not self.running:
            return

        self.speechProxy.say("While I came with built-in behaviors,"
                             " there's very little I can do without the"
                             " programs made by the students here at"
                             " Montana Tech; programming me is not easy,"
                             " but these students have been well-equipped"
                             " by their education here to deal with"
                             " complex problems.")
        time.sleep(1)

        self.currentStep += 1

        if not self.running:
            return

        self.speechProxy.say("I hope you have a pleasant and "
                             "informative visit here at Montana Tech.")
        time.sleep(1)

        self.currentStep += 1

        if not self.running:
            return

        self.speechProxy.say("Now I must return to my post."
                             "Have a nice day.")

        self.motions.lookForward()
        self.motions.turnAround()

        self.currentStep += 1

        if not self.running:
            return

        self.speechProxy.say("I'm looking for the mark on the shelves"
                             " to get back into the office.")
        if not self.motions.lookAroundForMark(64):
            self.fail()

        self.currentStep += 1

        if not self.running:
            return

        self.speechProxy.say("Ah! There it is.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(64, .35):
            self.fail()

        self.currentStep += 1

        if not self.running:
            return

        self.speechProxy.say("I will now return to my post,"
                             " using the mark on the water jug.")
        if not self.motions.lookAroundForMark(68):
            self.fail()

        self.currentStep += 1

        if not self.running:
            return

        self.speechProxy.say("Ah! I see the mark.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(68, .15):
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
#end TourDemoRoutine.py

demo = TourDemoRoutine()
demo.connect()
demo.run()
