# TicTacToe-FinalVersion

In this project you're able to play TicTacToe with DoBot by connected your computer with the DoBot and a VisionKit.

Needed tools:
* Playing field
* Playing pieces
* Windows computer (Tested on Windows 8)
* Python 3.6
* OpenCV library for Python

### How to play?

1. Download the repo
2. Set up DoBot
3. Set up VisionKit
4. Run the calibration 'python calibration.py' and follow the instructions.
5. Run 'python start.py' to start the game.

### Setting up the DoBot
If you need help setting up DoBot, follow this link.
<https://github.com/SERLatBTH/DobotMagician>
This project uses the suctioncup to pick up respective piece.

### Setting up the VisionKit

For the basic setup please visit the GitHub repo below.
<https://github.com/SERLatBTH/DobotMagicianVisionKit>
Place the camera support as high as possible on the extension pole. Position the camera so that the usb-port is pointing to the right when you're standing behind it.

To use the camera you'll need to install the two .exe files that's within the "CameraSetup" folder. 'driver_setup' installs the required drivers, 'usbVideo_setup' installs a couple of program, the one we're looking for is "DShowManager". Once you've installed both you need to open DShowManager and enable 'Auto register DS' and 'Keep Alive', this will let the computer find the camera.


### Playing field

The playing field used is 15x15cm and drawn on a regular piece of paper. The playing pieces were made out of cardboard with the size 4x4cm and has O's and X's ontop of them. Look at the picture below on how the playing field should be, the calibration program will help you place it in the correct spot. You can keep the paper in place by placing something heavy on it, or use some tape. Once the calibration stage is done you may put the pieces DoBot will use in a proper pile like the picture below. You may need to move the pile alittle bit away from the playing field if the DoBot does not align the pieces correctly when he places them.


#### Setup should look like this

![Everything set up](https://i.imgur.com/H5l4tLC.jpg "Everything set up")


My name is Pontus Andersson and I study Web Programming at Blekinge Institute of Technology.
This project was worked on for the course Software Engineering Project.
