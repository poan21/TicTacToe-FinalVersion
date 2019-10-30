from DobotMovement import DobotMovement
import cv2
""" Calibrates DoBot and board. Run before starting game """

def startCalibrate():
    dm = DobotMovement()

    print("Setting home location")
    dm.calibrate(1)
    input("Press enter when DoBot stops moving...")

    print(
    """
Please place the middle-right square in the playfield under the suction cup.

- - -
- - X
- - -
    """)

    dm.calibrate(2)
    input("Press enter when done...")
    print(
    """
Please place the middle-right square in the playfield under the suction cup

- - -
X - -
- - -
    """)

    dm.calibrate(3)
    input("Press enter when done...")

    ("Please coordinate the camera so that the left and bottom sides of the playing field are as close as possible to the bottom left corner of the camera. Adjust sharpness and light to make the picture as clear as possible.")
    print("Press q to quit the calibration")

    dm.moveAway()
    dm.disconnect()

    cap = cv2.VideoCapture(1)

    while(True):
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame',gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    print("You may now start the game with 'python start.py'")


if __name__ == "__main__":
    startCalibrate()
