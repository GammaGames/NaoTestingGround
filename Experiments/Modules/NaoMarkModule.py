# ********************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS: Python 2.7 on Windows 10
#
# DEVELOPED WITH: PyCharm Community 2016.2.3 on Windows 7
#
# AUTHORS: Unknown, Logan Warner
#
# DESCRIPTION: Module for Nao Mark Visual Functions
# ********************************************************
# -*- encoding: UTF-8 -*-

# --------------
# Pyhton imports
# --------------
import math

# -------------------
# Application imports
# -------------------
import almath

# ---------
# Functions
# ---------
def getMarkData (memoryProxyPR, landmarkProxyPR):
    """
    Returns a multidimensional array of naomark data
    :param memoryProxyPR:
    :param landmarkProxyPR:
    :return: markData
    """
    #Subscribe to landmarkDetected
    landmarkProxyPR.subscribe("GetLandMarkData")

    #Wait for a mark to be detected
    markData = memoryProxyPR.getData("LandmarkDetected")

    #Unsubscribe to proxy
    landmarkProxyPR.unsubscribe("GetLandMarkData")

    return markData

#Finds and returns a NaoMark's number
def getMarkNumber (markData):

    markNumber = markData[1][0][1][0]
    return markNumber

#Finds and returns the vertical and horiztontal
#offset of a nao mark relative to nao's camera
def getMarkAngles (markData):

    #Get the landmark positions(Relative to Camera)
    wzCamera = markData[1][0][0][1]
    wyCamera = markData[1][0][0][2]

    return wzCamera, wyCamera

#Finds and returns the x,y,z position of a nao mark
#relative to nao's camera
def getMarkXYZ (motionProxy, markData, landmarkSize):

    currentCamera = "CameraTop"

    # Retrieve landmark angular size in radians.
    angularSize = markData[1][0][0][3]

    # Compute distance to landmark.
    distanceFromCameraToLandmark =\
        landmarkSize / ( 2 * math.tan( angularSize / 2))

    # Retrieve landmark center position in radians.
    wzCamera = markData[1][0][0][1]
    wyCamera = markData[1][0][0][2]

    # Get current camera position in NAO space.
    transform = motionProxy.getTransform(currentCamera, 2, True)
    transformList = almath.vectorFloat(transform)
    robotToCamera = almath.Transform(transformList)

    # Compute the rotation to point towards the landmark.
    cameraToLandmarkRotationTransform =\
        almath.Transform_from3DRotation(0, wyCamera, wzCamera)

    # Compute the translation to reach the landmark.
    cameraToLandmarkTranslationTransform =\
        almath.Transform(distanceFromCameraToLandmark, 0, 0)

    # Combine all transformations to get the landmark position in NAO space
    robotToLandmark = robotToCamera *\
                      cameraToLandmarkRotationTransform *\
                      cameraToLandmarkTranslationTransform

    return robotToLandmark.r1_c4,\
           robotToLandmark.r2_c4, robotToLandmark.r3_c4