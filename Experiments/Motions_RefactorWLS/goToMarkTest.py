# -------------------
# Application imports
# -------------------
from motionsWLS import CustomMotions
from naoqi import ALProxy

# ----
# Main
# ----
def main():
    tts = ALProxy("ALTextToSpeech", "10.0.0.7", 9559)
    tts.say("It's time to get testing!")

    motions = CustomMotions()

    motions.standUp()

    tts.say("Hello!")
    motions.wave()

    tts.say("Now where oh where is mark 107?")
    motions.detectMarkWalkStraight(107)
    tts.say("Here it is.")
    tts.say("Now it's time to rest.")

    motions.sitDown()
#main

main()