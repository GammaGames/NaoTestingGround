# *************************************************************
# PROJECT: 	ShowRobbie2
#
# FILE:    	robbieSitDown.py
#
# DEVELOPMENT ENVIRONMENTS:
# Eclipse Neon.1 with PyDev  with Python 2.7.11
#
# EXECUTION ENVIRIONMENTS:
# Eclipse Neon.1 with PyDev with Python 2.7.11
#
# HARD COPY LISTING:
# Windows Programmer's Notepad
#
# HISTORY:
# Date        Author            Description
# ====        ======            ===========
# 10/05/16    J. Lieberg        Standards compliance
# **************************************************************
#
# -------------------
# Application imports
# -------------------
from naoqi import ALProxy
#
#-----------------
# Global constants
#-----------------
robotIP = "10.0.0.7"
PORT = 9559
#
# -------
# sitDown
# -------
def sitDown():
    """
    Wake up, sit down, and rest
    """

    '''
	----------------------------------------------------------
    REQUIREMENTS:
    R01 Robbie goes from the current pose to a sitting posture

    DESIGN:
    Algorithm
    ---------
    XXX IP and PORT constants defined at module level
    A01 Instantiate motionProxy;
        Instantiate postureProxy;
    A02 Invoke motionProxy.wakeup()
    A03 Invoke postureProxy.goToPosture("Sit", 1.0)
    A04 Invoke motion.Proxy.rest()
	-----------------------------------------------------------
	' ' '
	
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)         	#L01
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)
    
    motionProxy.wakeUp()                                      	#L02
    postureProxy.goToPosture("Sit", 1.0)                      	#L03
    motionProxy.rest()                                         	#L04
#def sitDown()

sitDown()

# end robbieSitDownSDP.py