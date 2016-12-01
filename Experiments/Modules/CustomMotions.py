# *******************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS: Python 2.7 on Windows 7
#
# DEVELOPED WITH: Pycharm 2016.2.3
#
# AUTHORS: Unknown, Logan Warner, Jessie Lieberg
#
# DESCRIPTION: Convenience functions for moving the robot
# *******************************************************

# --------------
# Python imports
# --------------
import math
import time

from naoqi import ALProxy

import NaoMarkModule


# -----------------
# Class and methods
# -----------------
class CustomMotions():
    """A module for all the motions defined by the Senior Design team"""
    def __init__(self, IP_PR="10.0.0.7", PORT_PR=9559):
        self.naoMarkSize = .12
        self.stepArray = [["StepHeight", 0.015], ["MaxStepX", 0.02],
                          ["MaxStepTheta", .18]]
        self.curAngle = 0
        self.motionProxy = ALProxy("ALMotion", IP_PR, PORT_PR)
        self.motionProxy.setStiffnesses("Body", 1)
        self.motionProxy.\
            setExternalCollisionProtectionEnabled("All", False)
        self.postureProxy = ALProxy("ALRobotPosture", IP_PR, PORT_PR)
        self.memoryProxy = ALProxy("ALMemory", IP_PR, PORT_PR)
        self.landmarkProxy = ALProxy("ALLandMarkDetection", IP_PR, PORT_PR)
        self.tts = ALProxy("ALTextToSpeech", IP_PR, PORT_PR)
    #__init__ (default constructor)

    def standUp(self, speedPR=1):
        self.motionProxy.wakeUp()
        self.postureProxy.goToPosture("StandInit", speedPR)
    #standUp

    def sitDown(self, speedPR=1):
        self.motionProxy.wakeUp()
        self.postureProxy.goToPosture("Sit", speedPR)
    #standUp

    def wave(self, async=False):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.8, 1.56, 2.24, 2.8, 3.48, 4.6])
        keys.append([0.29602, -0.170316, -0.340591,
                     -0.0598679, -0.193327, -0.01078])

        names.append("HeadYaw")
        times.append([0.8, 1.56, 2.24, 2.8, 3.48, 4.6])
        keys.append([-0.135034, -0.351328, -0.415757,
                     -0.418823, -0.520068, -0.375872])

        names.append("LElbowRoll")
        times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
        keys.append([-1.37902, -1.29005, -1.18267,
                     -1.24863, -1.3192, -1.18421])

        names.append("LElbowYaw")
        times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
        keys.append([-0.803859, -0.691876, -0.679603,
                     -0.610574, -0.753235, -0.6704])

        names.append("LHand")
        times.append([1.48, 4.52])
        keys.append([0.238207, 0.240025])

        names.append("LShoulderPitch")
        times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
        keys.append([1.11824, 0.928028, 0.9403,
                     0.862065, 0.897349, 0.842125])

        names.append("LShoulderRoll")
        times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
        keys.append([0.363515, 0.226991, 0.20398,
                     0.217786, 0.248467, 0.226991])

        names.append("LWristYaw")
        times.append([1.48, 4.52])
        keys.append([0.147222, 0.11961])

        names.append("RElbowRoll")
        times.append([0.64, 1.4, 1.68, 2.08, 2.4,
                      2.64, 3.04, 3.32, 3.72, 4.44])
        keys.append([1.38524, 0.242414, 0.349066, 0.934249, 0.680678,
                     0.191986, 0.261799, 0.707216, 1.01927, 1.26559])

        names.append("RElbowYaw")
        times.append([0.64, 1.4, 2.08, 2.64, 3.32, 3.72, 4.44])
        keys.append([-0.312978, 0.564471, 0.391128, 0.348176,
                     0.381923, 0.977384, 0.826783])

        names.append("RHand")
        times.append([1.4, 3.32, 4.44])
        keys.append([0.853478, 0.854933, 0.425116])

        names.append("RShoulderPitch")
        times.append([0.64, 1.4, 2.08, 2.64, 3.32, 4.44])
        keys.append([0.247016, -1.17193, -1.0891,
                     -1.26091, -1.14892, 1.02015])

        names.append("RShoulderRoll")
        times.append([0.64, 1.4, 2.08, 2.64, 3.32, 4.44])
        keys.append([-0.242414, -0.954191, -0.460242,
                     -0.960325, -0.328317, -0.250085])

        names.append("RWristYaw")
        times.append([1.4, 3.32, 4.44])
        keys.append([-0.312978, -0.303775, 0.182504])

        if async:
            self.motionProxy.post.angleInterpolation(
                names, keys, times, True)
        else:
            self.motionProxy.angleInterpolation(names, keys, times, True)
    #wave

    def turnLeft(self, degreesPR):
        self.motionProxy.moveInit()
        self.motionProxy.setMoveArmsEnabled(True, True)
        time.sleep(1)
        self.motionProxy.moveTo(0, 0,
                                math.radians(degreesPR), self.stepArray)
    #turnLeft

    def turnRight(self, degreesPr):
        self.turnLeft(-degreesPr)
    #turnRight

    def turnAround(self, directionrPR="left"):
        if directionrPR == "left":
            self.turnLeft(180)
        else:
            self.turnRight(180)
    #turnAround

    def lookAround(self):
        self.motionProxy.moveInit()
        time.sleep(1)

        names = "HeadYaw"
        angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
        times = [1.0,  2.0, 3.0,  4.0, 5.0]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists,
                                            times, isAbsolute)
    #lookAround

    def lookTo(self, degreesPR):
        self.motionProxy.moveInit()
        time.sleep(1)

        self.motionProxy.setAngles("HeadYaw", math.radians(degreesPR), .1)
    #lookTo

    def lookForward(self):
        self.lookTo(0)

    def lookAroundForMark(self, markNumPR=None):
        self.motionProxy.moveInit()
        time.sleep(1)

        names = "HeadYaw"
        markFound = False
        headAngle = .25
        back = False
        markData = NaoMarkModule.getMarkData(self.memoryProxy,
                                             self.landmarkProxy)
        first = True

        while not markFound:
            if back:
                headAngle -= .125
            else:
                headAngle += .125

            if abs(headAngle) > 1.0:
                headAngle = max(min(headAngle, 1), -1)
                back = ~back

            times = .15
            if first:
                times = 1.0
            isAbsolute = True
            self.motionProxy.angleInterpolation(names, headAngle,
                                                times, isAbsolute)

            markData = NaoMarkModule.getMarkData(self.memoryProxy,
                                                 self.landmarkProxy)

            if not (markData is None or len(markData) == 0):
                if markNumPR is None or\
                        (NaoMarkModule.getMarkNumber(markData) ==
                             markNumPR):
                    markFound = True
            first = False
        return markData
    #lookAroundForMark

    def lookAroundForMarkMoving(self, markNumPR):
        self.motionProxy.moveInit()
        time.sleep(1)

        names = "HeadYaw"
        markFound = False
        headAngle = .25
        back = False
        markData = NaoMarkModule.getMarkData(self.memoryProxy,
                                             self.landmarkProxy)
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
            self.motionProxy.angleInterpolation(names, headAngle, times,
                                           isAbsolute)

            markData = NaoMarkModule.getMarkData(self.memoryProxy,
                                                 self.landmarkProxy)

            if not (markData is None or len(markData) == 0):
                if markNumPR is None or\
                        (NaoMarkModule.getMarkNumber(markData) ==
                             markNumPR):
                    markFound = True
            first = False
        return markData
    #lookAroundForMarkMoving

    def detectMarkSearch(self, number, directionPR="forward"):
        markD = None
        searching = True
        while searching:
            markD = CustomMotions.lookAroundForMarkMoving(self, number)
            if not (markD is None or len(markD) == 0):
                 print "found something"
                 searching = False
            else:
                print "tried turn"
                CustomMotions.turnRight30(self)

        x, y, z = NaoMarkModule.getMarkXYZ(self.motionProxy, markD,
                                           self.naoMarkSize)

        if directionPR == "l":
            CustomMotions.moveForwardY(self, x, y + .35)
        elif directionPR == "s":
            CustomMotions.moveForwardY(self, x, y - .35)
        else:
            CustomMotions.moveForwardY(self, x, y)
    #detectMarkSearch

    def turnToLookAngle(self):
        self.motionProxy.moveInit()
        time.sleep(1)
        global curAngle

        angle = self.motionProxy.getAngles("HeadYaw", False)
        print angle[0]

        self.motionProxy.moveTo(0, 0, angle[0])
        print "Turned to look angle"
    #turnToLookAngle

    # Non-0 theta is strafing according to old code
    def moveForward(self, distance, y=0, theta=0):
        self.motionProxy.moveInit()
        self.motionProxy.setMoveArmsEnabled(True, True)
        time.sleep(1)
        print "moving x:" + str(distance) + "y " + str(y)
        self.motionProxy.moveTo(distance, y, theta, self.stepArray)
    #moveForward

    def detectMarkAndMoveTo(self, markNumPR=None, offsetY=0):
        markD = CustomMotions.lookAroundForMark(self, markNumPR)
        x, y, z = NaoMarkModule.getMarkXYZ(self.motionProxy, markD,
                                           self.naoMarkSize)
        CustomMotions.moveForward(self, x - .15, y + offsetY)
    #detectMarkAndMoveTo

    def detectMarkWalkStraight(self, markNumPR=None):
        CustomMotions.turnToLookAngle(self)
        CustomMotions.detectMarkAndMoveTo(self, markNumPR)
    #detectMarkWalkStraight
#end CustomMotions.py