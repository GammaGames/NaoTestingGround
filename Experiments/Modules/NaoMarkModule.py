# ********************************************************
# PROJECT: ShowRobbie2
#
# EXECUTION ENVIRONMENTS:
# Python 2.7 on Windows 10,
# Python 2.7 on Windows 7
#
# DEVELOPED WITH:
# PyCharm Community 2016.2.3 on Windows 7,
# PyCharm Community 2016.3 on Manjaro Linux
#
# AUTHORS: Unknown, Logan Warner
#
# DESCRIPTION: Module for Nao Mark Visual Functions
# ********************************************************
# -*- encoding: UTF-8 -*-

# --------------
# Python imports
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
    Returns a multidimensional list of NAO mark data
    :param memoryProxyPR: memory proxy
    :param landmarkProxyPR: landmark proxy
    :return: markData
    """
    '''
    REQUIREMENTS:
    R01 The NAO robot must detect a landmark
    R02 The function must return a 4-dimensional array containing
          data on the landmark

    DESIGN:

    Algorithm
    ---------
    A01 Call subscribe on landmarkProxy with "GetLandMarkData"
    A02 Instantiate markData with blocking call to getData on
          memoryProxy with "LandmarkDetected"
    A03 Call unsubscribe on landmarkProxy with "GetLandMarkData"
    A04 Return markData
    '''
    #Subscribe to landmarkDetected
    landmarkProxyPR.subscribe("GetLandMarkData")                       #L01

    #Wait for a mark to be detected
    markData = memoryProxyPR.getData("LandmarkDetected")

    #Unsubscribe to proxy
    landmarkProxyPR.unsubscribe("GetLandMarkData")

    return markData
#getMarkData

#Finds and returns a NaoMark's number
def getMarkNumber (markDataPR):
    """
    Finds and returns a NaoMark's number
    :param markDataPR: 4-dimensional list containing data on the mark
    """
    '''
    REQUIREMENTS:
    R01 Must return the ID number of the mark from the mark data
          passed in

    DESIGN:

    Algorithm
    ---------
    A01 Return item in a spot in the 4-dimensional list,
        which is the mark number
    '''
    markNumber = markDataPR[1][0][1][0]                                #L01
    return markNumber
#getMarkNumber

#Finds and returns the vertical and horiztontal
#offset of a nao mark relative to nao's camera
def getMarkAngles (markDataPR):
    """
    Returns the vertical and horizontal offset of a nao mark in
    radiansrelative to nao's camera from the mark data
    :param markDataPR: 4-dimensional list containing data on the mark
    """
    '''
    REQUIREMENTS:
    R01 Must return the vertical and horizontal offsets of the NAO
        mark in radians

    DESIGN:

    Algorithm
    ---------
    A01 Return the vertical and horizontal offset from the
        associated spots in the 4-dimensional list markDataPR
    '''
    #Get the landmark positions(Relative to Camera)
    wzCamera = markDataPR[1][0][0][1]
    wyCamera = markDataPR[1][0][0][2]

    return wzCamera, wyCamera
#getMarkAngles

#Finds and returns the x,y,z position of a nao mark
#relative to nao's camera
def getMarkXYZ (motionProxyPR, markDataPR, landmarkSizePR):
    """
    Finds and returns the x,y,z position of a nao mark
    relative to nao's camera
    :param motionProxyPR:
    :param markDataPR:
    :param landmarkSizePR:
    """
    '''
    REQUIREMENTS:
    R01 Must return x, y, and z coordinates of the mark relative to
          the NAO

    DESIGN:

    Algorithm
    ---------
    A01 Instantiate currentCamera string
    A02 Instantiate angularSize (in radians)
          from a spot in the 4-dimensional list markDataPR
    A03 Instantiate distanceToLandmark by calculating from the angle
    A04 Instantiate wzCamera and wyCamera as the
          vertical and horizontal offset, respectively,
          of the mark in radians
    A05 Instantiate transform representing position of camera in
          NAO space
    A06 Instantiate transformList
    A07 Instantiate robotToCamera as the transform
          to get robot position from the camera position
    A08 Instantiate cameraToLandmarkRotationTransform as the
          transform to rotate to point at the landmark
    A09 Instantiate cameraToLandmarkTranslationTransform as the
          transform to move tot he landmark
    A10 Instantiate robotToLandmark as the combined transformations
    A11 Return x, y, and z coordinates of the transform
    '''
    currentCamera = "CameraTop"                                        #L01

    angularSize = markDataPR[1][0][0][3]                               #L02
    distanceToLandmark = landmarkSizePR / \
                         (2 * math.tan(angularSize / 2))               #L03

    wzCamera, wyCamera = getMarkAngles(markDataPR)                     #L04

    transform = motionProxyPR.getTransform(currentCamera, 2, True)     #L05
    transformList = almath.vectorFloat(transform)                      #L06
    robotToCamera = almath.Transform(transformList)                    #L08

    cameraToLandmarkRotationTransform = \
        almath.Transform_from3DRotation(0, wyCamera, wzCamera)         #L09
    cameraToLandmarkTranslationTransform = \
        almath.Transform(distanceToLandmark, 0, 0)                     #L10

    robotToLandmark = robotToCamera * \
                      cameraToLandmarkRotationTransform * \
                      cameraToLandmarkTranslationTransform             #L11

    return robotToLandmark.r1_c4, \
           robotToLandmark.r2_c4, robotToLandmark.r3_c4                #L12
#getMarkXYZ

#end naoMarkModule.py