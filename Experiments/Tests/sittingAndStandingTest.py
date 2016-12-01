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

    tts.say("Time for a little stretch of the legs.")
    motions.standUp()
    motions.sitDown()
# main

main()