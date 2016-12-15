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
    tts.say("It's time to get testing!")

    motions = CustomMotions()

    motions.standUp()

    tts.say("Now where oh where is mark 80?")
    motions.detectMarkWalkStraight(80)
    tts.say("Here it is.")
    tts.say("Now it's time to rest.")

    motions.sitDown()
#main

main()