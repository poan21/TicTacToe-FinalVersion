# TicTacToe-FinalVersion

In this project you're able to play TicTacToe with DoBot by connected your computer with the DoBot and a VisionKit.

Needed tools:
* Playing field
* Playing pieces
* Windows computer (Tested on Windows 8)
* Python 3.6
* OpenCV library for Python

## Setting up the VisionKit

For the basic setup please visit the GitHub repo below.
<https://github.com/SERLatBTH/DobotMagicianVisionKit>
Place the camera support as high as possible on the extension pole. Position the camera so that the usb-port is pointing to the right when you're standing behind it.

To use the camera you'll need to install the two .exe files that's within the "CameraSetup" folder. 'driver_setup' installs the required drivers, 'usbVideo_setup' installs a couple of program, the one we're looking for is "DShowManager". Once you've installed both you need to open DShowManager and enable 'Auto register DS' and 'Keep Alive', this will let your computer use the VisionKit as a regular webcam.


### Playing field

The playing field used is 15x15cm and drawn on a regular piece of paper. The playing pieces were made out of cardboard with the size 4x4cm and has O's and X's ontop of them.


### How to play?

1. Download the repo
2. Set up VisionKit
3. Run the calibration 'python calibration.py' and follow the instructions.
4. Run 'python start.py' to start the game.
5. Enjoy!


My name is Pontus Andersson and I study Web Programming at Blekinge Institute of Technology.
This project was worked on for the course Software Engineering Project.
