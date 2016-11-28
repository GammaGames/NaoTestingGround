# -------------------
# Application imports
# -------------------
from motionsWLS import CustomMotions
from naoqi import ALProxy
from BrokerController import BrokerController
from BotFreezerModule import BotFreezerModule

# ----------------
# Global constants
# ----------------
robotIP = "10.0.0.7"
PORT = 9559

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
FootFreezer = None

# ----
# Main
# ----
def main():
    global brokyControlly
    brokyControlly = BrokerController()
    brokyControlly.createBroker()

    global BotFreezer
    BotFreezer = BotFreezerModule("BotFreezer")

    global cmModule
    cmModule = CustomMotions("cmModule")
    cm = ALProxy("cmModule")

    motionProxy.setStiffnesses("Body", 1)
    postureProxy.goToPosture("StandInit", 1)

    motionProxy.setExternalCollisionProtectionEnabled("All", False)
    movementResult = cm.post.turnLeft(45)
    cm.wait(movementResult, 0)
    movementResult = cm.post.turnRight(45)
    cm.wait(movementResult, 0)
    movementResult = cm.post.turnAround("left")
    cm.wait(movementResult, 0)
    movementResult = cm.post.turnAround("right")
    cm.wait(movementResult, 0)
    movementResult = cm.post.lookTo(45)
    cm.wait(movementResult, 0)
    movementResult = cm.post.detectMarkWalkStraight(107)
    cm.wait(movementResult, 0)
#main

main()