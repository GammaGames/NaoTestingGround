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

    tts.say("Hello")
    motions.wave()

    motions.sitDown()
#main

main()