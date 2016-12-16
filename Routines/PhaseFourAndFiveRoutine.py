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
# DESCRIPTION: Phase 4 and 5 of the tour demo
# **************************************************************

# -------------------
# Application imports
# -------------------
from CustomMotions import CustomMotions
from naoqi import ALProxy
from NaoTestingGround import Routine


class PhaseFourAndFiveRoutine(Routine.Routine):
    '''
    Tour demo phases 4 and 5
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 7
    # __init__

    def connect(self, IP_PR="10.0.0.7", port_PR=9559):
        self.speechProxy = ALProxy("ALTextToSpeech", IP_PR, port_PR)
        self.autonomousLifeProxy = ALProxy("ALAutonomousLife",
                                           IP_PR, port_PR)
        # IP and port overridden in case they change
        self.motions = CustomMotions(IP_PR, port_PR)
    #connect

    def perform(self):
        self.autonomousLifeProxy.setState("disabled")

        self.motions.sitDown()
        self.speechProxy.say("I've got to go back now.")

        self.motions.standUp()
        self.speechProxy.say("Going to stretch my legs a little"\
                             " to get a feel for the carpet")

        self.motions.turnLeft(.2)
        self.motions.turnRight(.2)

        self.motions.turnAround()
        self.speechProxy.say("I must now find the mark to get back into the office.")
        if not self.motions.lookAroundForMark(64):
            self.fail()

        self.speechProxy.say("Ah! I see it.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(
                64, stoppingDistancePR=.35):
            self.fail()

        self.speechProxy.say("I will now return to my post. Mark 68 marks it.")
        if not self.motions.lookAroundForMark(68):
            self.fail()

        self.speechProxy.say("Ah! I see the mark.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(
                68, stoppingDistancePR=.2):
            self.fail()
        self.motions.turnAround()
        self.motions.sitDown()
    #run

    def fail(self):
        self.speechProxy.say("I couldn't find the mark.")
        self.motions.sitDown()
        self.running = False
    #fail
#end PhaseFourAndFiveRoutine.py