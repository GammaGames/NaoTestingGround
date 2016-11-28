# ***************************************************************
# PROJECT: 	ShowRobbie2
#
# FILE: 	robbieSpeechSpielSDP
#
# DEVELOPMENT ENVIRONMENTS:
# Pycharm 2016.2 on Windows
#
# EXECUTION ENVIRONMENTS: 
# Python 2.7 on Windows 7
#
# HARD COPY LISTING:
# Windows as noted in page title
#
# HISTORY:
# Date		Author		Description
# 10/20/16	L. Warner	Initial standard version
#
# NOTE 1:
# Setting the volume ('tts.setVolume(0.00001)') does not seem to 
# work
# NOTE 2:
# 11/15/16 - there are no known conditions for which this module
# cannot be run if no other modules are active.
# **************************************************************

# -------------------
# Application imports
# -------------------
from naoqi import ALProxy

#-----------------
# Global constants
#-----------------
IP = "10.0.0.7"												    #L01
PORT = 9559

# -----------------
# robbieSpeechSpiel
# -----------------
def robbieSpeechSpiel():
    """
    Simple text to speech giving a spiel about what she is.
    """
    '''
    REQUIREMENTS:
    R01 Robbie says a greeting message

	DESIGN
    Algorithm
    ---------
	A01	IP and PORT global constants set at global level;
    A02 Instantiate tts as an ALTextToSpeech proxy using IP and PORT;
    A03 Say greeting message;
    A04 Return;
    '''

    tts = ALProxy("ALTextToSpeech", IP, PORT)               	#L02
    tts.say("Hello, I am Robbie.")                           	#L03
    tts.say("I'm a NAO robot. I'm designed and manufactured by ")
    tts.say("the Aldebaran company in France.")
    return                                                      #L04
#def robbieSpeechSpielSDP

robbieSpeechSpiel()

#end robbieSpeechSpielSDP.py