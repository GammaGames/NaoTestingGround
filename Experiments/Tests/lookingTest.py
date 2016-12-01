# -------------------
# Application imports
# -------------------
from naoqi import ALProxy

from CustomMotions import CustomMotions


# ----
# Main
# ----
def main():
    tts = ALProxy("ALTextToSpeech", "10.0.0.7", 9559)

    motions = CustomMotions()

    motions.standUp()


    motions.lookTo(60)
    tts.say("To the left to the left.")
    motions.turnToLookAngle()
    tts.say("And back.")
    motions.turnRight(60)

    motions.sitDown()


# main

main()