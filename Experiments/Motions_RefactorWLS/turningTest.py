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
    motions = CustomMotions()
    motions.standUp()
    tts.say("Let's make sure I can turn.")
    motions.turnLeft(45)
    motions.turnRight(45)
    motions.turnAround("left")
    motions.turnAround("right")
    motions.sitDown()
#main

main()