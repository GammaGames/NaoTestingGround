# *******************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS: Python 2.7 on Windows 7
#
# DEVELOPED WITH:
# Pycharm 2016.2.3 on Windows 10,
# Pycharm 2016.2.3 on Windows 7,
# Pycharm 2016.3 on Windows 7,
# Github webapp text editor
#
# AUTHORS: Unknown, Logan Warner, Jesse Lieberg
#
# DESCRIPTION: Convenience functions for moving the robot
# *******************************************************

# --------------
# Python imports
# --------------
import math

# -------------------
# Application imports
# -------------------
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

    def turnLeft(self, radiansPR):
        self.motionProxy.wakeUp()
        self.motionProxy.\
            setExternalCollisionProtectionEnabled("All", False)
        self.motionProxy.setMoveArmsEnabled(True, True)
        if abs(radiansPR) > .17:
            self.motionProxy.moveTo(0, 0, radiansPR, self.stepArray)
    #turnLeft

    def turnRight(self, radiansPr):
        self.turnLeft(-radiansPr)
    #turnRight

    def turnAround(self, directionrPR="left"):
        if directionrPR == "left":
            self.turnLeft(math.pi)
        else:
            self.turnRight(math.pi)
    #turnAround

    def lookAround(self):
        self.motionProxy.wakeUp()

        names = "HeadYaw"
        angleLists = [1.0, -1.0, 1.0, -1.0, 0.0]
        times = [1.0,  2.0, 3.0,  4.0, 5.0]
        isAbsolute = True
        self.motionProxy.angleInterpolation(names, angleLists,
                                            times, isAbsolute)
    #lookAround

    def lookTo(self, radiansHorizontalPR, radiansVerticalPR=0):
        self.motionProxy.wakeUp()
        self.motionProxy.setAngles("HeadYaw",
                                   radiansHorizontalPR, .1)
        self.motionProxy.setAngles("HeadPitch",
                                   radiansVerticalPR, .1)
    #lookTo

    def lookForward(self):
        self.motionProxy.wakeUp()
        self.lookTo(0)
    #lookForward

    def lookAroundForMark(self, markNumPR=None, maxAttemptsPR=4):
        self.motionProxy.wakeUp()

        headAngle = 0
        back = False
        attempts = 0
        incrementAngle = math.pi/12
        maxAngle = math.pi/2
        markData = None
        while not attempts >= maxAttemptsPR:
            markData = NaoMarkModule.getMarkData(self.memoryProxy,
                                                 self.landmarkProxy)
            if not markData or len(markData) == 0:
                markData = None
            if markData is not None:
                if markNumPR is None or\
                   (NaoMarkModule.getMarkNumber(markData) == markNumPR):
                    break

            if back:
                headAngle -= incrementAngle
            else:
                headAngle += incrementAngle

            if abs(headAngle) > maxAngle:
                headAngle = max(min(headAngle, maxAngle), -maxAngle)
                back = ~back
                attempts += 1
            self.motionProxy.angleInterpolation("HeadYaw", headAngle,
                                                attempts+1*.5, True)
        #while not reached maximum attempts
        return markData
    #lookAroundForMark

    def walkTo(self, x, y=0, theta=0):
        self.motionProxy.wakeUp()
        self.motionProxy.setExternalCollisionProtectionEnabled("All",
                                                               False)
        self.motionProxy.setMoveArmsEnabled(True, True)
        print "Moving to x:{}, y:{} meters from NAO position".format(x, y)
        self.motionProxy.moveTo(x, y, theta, self.stepArray)
    #moveForward

    def getLookAngle(self):
        return self.motionProxy.getAngles("HeadYaw", True)[0]
    #getLookAngle

    def turnToLookAngle(self):
        self.turnLeft(self.getLookAngle())
    #turnToLookAngle

    def detectMarkAndMoveTo(self, markNumPR=None,
                            stoppingDistancePR=.25, lateralOffsetPR=0,
                            walkStraightPR=True):
        markData = self.lookAroundForMark(markNumPR)
        if markData is None:
            print "Mark not found!"
            return False

        if walkStraightPR:
            while abs(self.getLookAngle()) > math.pi/12:
                markData = self.lookAroundForMark(markNumPR)
                self.turnToLookAngle()
        x, y, z = NaoMarkModule.getMarkXYZ(self.motionProxy, markData,
                                           self.naoMarkSize)
        print "Mark detected at x:{}, y:{} meters from NAO position"\
              .format(x, y)
        self.walkTo(x - stoppingDistancePR,
                    y + lateralOffsetPR)
        return True
    #detectMarkAndMoveTo
#end CustomMotions.py
