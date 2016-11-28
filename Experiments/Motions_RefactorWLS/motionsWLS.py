# *******************************************************
# PROJECT:
#
# EXECUTION ENVIRONMENTS: Python 2.7 on Windows 7
#
# DEVELOPED WITH: Pycharm 2016.2.3
#
# AUTHORS: Unknown, Logan Warner
#
# DESCRIPTION: Convenience functions for moving the robot
# *******************************************************

# --------------
# Python imports
# --------------
import time
import math

# -------------------
# Application imports
# -------------------
import NaoMarkModule
from naoqi import ALModule
from naoqi import ALProxy

# ----------------
# Global constants
# ----------------
robotIP = "10.0.0.7"
PORT = 9559
naomarkSize = .12
stepArray = [["StepHeight", 0.015],["MaxStepX", 0.02],
             ["MaxStepTheta", .18]]

# ----------------
# Global variables
# ----------------
postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
lifeProxy = ALProxy("ALAutonomousLife", robotIP, PORT)
tts = ALProxy("ALTextToSpeech", robotIP, PORT)
motionProxy = ALProxy("ALMotion", robotIP, PORT)
curAngle = 0
BotFreezer = None
cmModule = None


class CustomMotions(ALModule):
    """A module for all the motions defined by the Senior Design team"""

    def turnLeft(self, degreesPR):
        motionProxy.moveInit()
        motionProxy.setMoveArmsEnabled(True, True)
        time.sleep(1)
        motionProxy.moveTo(0, 0, math.radians(degreesPR), stepArray)

    def turnRight(self, degreesPr):
        self.turnLeft(-degreesPr)

    def turnAround(self, directionrPR="left"):
        if directionrPR == "left":
            self.turnLeft(180)
        else:
            self.turnRight(180)

    def lookAround(self):
        motionProxy.moveInit()
        time.sleep(1)

        names = "HeadYaw"
        angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
        times = [1.0,  2.0, 3.0,  4.0, 5.0]
        isAbsolute = True
        motionProxy.angleInterpolation(names, angleLists, times,
                                       isAbsolute)

    def lookTo(self, degreesPR):
        motionProxy.moveInit()
        time.sleep(1)

        motionProxy.setAngles("HeadYaw", math.radians(degreesPR), .1)

    def lookAroundForMark(self, markNumPR=None):
        motionProxy.moveInit()
        time.sleep(1)

        names = "HeadYaw"
        markFound = False
        headAngle = .25
        back = False
        markData = NaoMarkModule.getMarkData(robotIP, PORT)
        first = True

        while not markFound:
            if back:
                headAngle = headAngle -.125
            else:
                headAngle = headAngle + .125

            if abs(headAngle) > 1.0:
                headAngle = max(min(headAngle, 1), -1)
                back = ~back

            times = .15
            if first:
                times = 1.0
            isAbsolute = True
            motionProxy.angleInterpolation(names, headAngle, times,
                                           isAbsolute)

            markData = NaoMarkModule.getMarkData(robotIP, PORT)

            if not (markData is None or len(markData) == 0):
                if markNumPR is None or\
                        (NaoMarkModule.getMarkNumber(markData) ==
                             markNumPR):
                    markFound = True
            first = False
        return markData

    def lookAroundForMarkMoving(self, number):
        motionProxy.moveInit()
        time.sleep(1)

        names = "HeadYaw"
        markFound = False
        headAngle = .25
        back = False
        markData = NaoMarkModule.getMarkData(robotIP, PORT)
        first = True
        attempts = 0

        while not markFound:
            # TODO REPLACE THIS NONSENSE
            if attempts >=4:
                return None
            if back:
                headAngle = headAngle -.125
            else:
                headAngle = headAngle + .125

            if abs(headAngle) > 1.0:
                headAngle = max(min(headAngle, 1), -1)
                back = ~back
                attempts = attempts + 1

            times = .15
            if first:
                times = 1.0
            isAbsolute = True
            motionProxy.angleInterpolation(names, headAngle, times,
                                           isAbsolute)

            markData = NaoMarkModule.getMarkData(robotIP, PORT)

            if not (markData is None or len(markData) == 0):
                if NaoMarkModule.getMarkNumber(markData) == number:
                    markFound = True
            first = False
        return markData

    def detectMarkSearch(self, number, directionPR="forward"):
        markD = None
        searching = True
        global naomarkSize
        global robotIP
        global PORT
        while searching:
            markD = CustomMotions.lookAroundForMarkMoving(self, number)
            if not (markD is None or len(markD) == 0):
                 print "found something"
                 searching = False
            else:
                print "tried turn"
                CustomMotions.turnRight30(self)

        x, y, z = NaoMarkModule.getMarkXYZ(robotIP, PORT, markD,
                                           naomarkSize)

        if directionPR == "l":
            CustomMotions.moveForwardY(self, x, y + .35)
        elif directionPR == "s":
            CustomMotions.moveForwardY(self, x, y - .35)
        else:
            CustomMotions.moveForwardY(self, x, y)

    def turnToLookAngle(self):
        motionProxy.moveInit()
        time.sleep(1)
        global curAngle

        angle = motionProxy.getAngles("HeadYaw", False)
        print angle[0]

        motionProxy.moveTo(0, 0, angle[0])
        print "Turned to look angle"

    # Non-0 theta is strafing according to old code
    def moveForward(self, distance, y=0, theta=0):
        motionProxy.moveInit()
        motionProxy.setMoveArmsEnabled(True, True)
        time.sleep(1)
        print "moving x:" + str(distance) + "y " + str(y)
        motionProxy.moveTo(distance, y, theta, stepArray)

    def detectMarkAndMoveTo(self, markNumPR=None, offsetY=0):
        markD = CustomMotions.lookAroundForMark(self, markNumPR)
        x, y, z = NaoMarkModule.getMarkXYZ(robotIP, PORT, markD,
                                           naomarkSize)
        CustomMotions.moveForward(self, x - .15, y + offsetY)

    def detectMarkWalkStraight(self, markNumPR=None):
        global naomarkSize
        CustomMotions.turnToLookAngle(self)
        CustomMotions.detectMarkAndMoveTo(self, markNumPR)

#end motionsWLS.py