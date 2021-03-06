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
# DESCRIPTION: Phase 1 and 2 of the tour demo
# **************************************************************

# -------------------
# Application imports
# -------------------
from CustomMotions import CustomMotions
from naoqi import ALProxy
from NaoTestingGround import Routine


class PhaseOneAndTwoRoutine(Routine.Routine):
    '''
    Tour demo phases 1 and 2
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.numberSteps = 14
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
        self.speechProxy.say("Thank you for waking me,"\
                             " I have a job to do.")

        self.motions.standUp()
        self.speechProxy.say("Going to stretch my legs a little"\
                             " to get a feel for the carpet")

        self.motions.turnLeft(.2)
        self.motions.turnRight(.2)

        self.speechProxy.say("I must now find the mark on the railing.")
        if not self.motions.lookAroundForMark(107):
            self.fail()

        self.speechProxy.say("Ah! I see the railing mark.")
        markSeenAngle = self.motions.getLookAngle()
        self.motions.turnLeft(markSeenAngle)
        if not self.motions.detectMarkAndMoveTo(107, 1):
            self.fail()

        self.motions.sitDown()
    #run

    def fail(self):
        self.speechProxy.say("I couldn't find the mark.")
        self.motions.sitDown()
        self.running = False
    #fail
#end PhaseOneAndTwoRoutine.py
