# -------------------
# Application imports
# -------------------
from motionsWLS import CustomMotions
from naoqi import ALProxy
from BrokerController import BrokerController
from BotFreezerModule import BotFreezerModule

# ----
# Main
# ----
def main():
    #tts = ALProxy("ALTextToSpeech", robotIP, PORT)

    motions = CustomMotions()

    motions.standUp(1)

    # motions.turnLeft(45)
    # motions.turnRight(45)
    # motions.turnAround("left")
    # motions.turnAround("right")
    motions.lookTo(45)
    motions.detectMarkWalkStraight(107)
    motions.lookTo(0)

    motions.sitDown(1)
#main

main()