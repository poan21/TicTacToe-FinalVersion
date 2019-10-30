import threading
import DobotDllType as dType

CON_STR = {
    dType.DobotConnect.DobotConnect_NoError:  "Dobot is connected without Errors",
    dType.DobotConnect.DobotConnect_NotFound: "Dobot can't be found",
    dType.DobotConnect.DobotConnect_Occupied: "Dobot is occupied"}

""" Module with Dobot class """

class DobotMovement():
    """ Handles DoBot movement """

    def __init__(self):
        self.api = dType.load()
        self.pieces = 5
        state = dType.ConnectDobot(self.api, "", 115200)[0]

        print("Connect status:",CON_STR[state])

        if state != dType.DobotConnect.DobotConnect_NoError:
            exit()

        dType.SetHOMEParams(self.api, 250, 0, 50, 0, isQueued = 1)
        dType.SetPTPJointParams(self.api, 200, 200, 200, 200, 200, 200, 200, 200, isQueued = 1)
        dType.SetPTPCommonParams(self.api, 100, 100, isQueued = 1)

    def home(self):
        """ Send arm to home position """

        dType.SetQueuedCmdClear(self.api)

        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, 0, 50, 0, isQueued = 1)

        dType.SetHOMECmd(self.api, temp = 0, isQueued = 1)
        dType.SetQueuedCmdStartExec(self.api)
        dType.DisconnectDobot(self.api)

    def hover(self):
        """ Hover in the air """

        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, 0, 50, 0)

    def placePos(self, spot):
        """ Takes argument spot as where to place it, and calls function placeIt with respective coords """

        if spot == 0:
            self.placeIt(300, 50, -55)
        elif spot == 1:
            self.placeIt(300, 0, -55)
        elif spot == 2:
            self.placeIt(300, -50, -55)
        elif spot == 3:
            self.placeIt(250, 50, -55)
        elif spot == 4:
            self.placeIt(250, 0, -55)
        elif spot == 5:
            self.placeIt(250, -50, -55)
        elif spot == 6:
            self.placeIt(200, 50, -55)
        elif spot == 7:
            self.placeIt(200, 0, -55)
        elif spot == 8:
            self.placeIt(200, -50, -55)

        self.moveAway()

    def placeIt(self, x, y, z, r=-40):
        """ Places it at coordinates given """
        # dType.SetQueuedCmdClear(self.api)
        self.pick()

        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, x, y, z, r, isQueued = 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, x, y, -62, r, isQueued = 1)
        dType.SetEndEffectorSuctionCup(self.api, 0, 1)
        dType.SetWAITCmd(self.api, 0.5, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, x, y, z, r, isQueued = 1)

        # dType.SetQueuedCmdStartExec(self.api)

    def pick(self):
        """ Pick up playpiece from stack """

        stackHeight = (self.pieces*3)-68
        r = -40

        # dType.SetQueuedCmdClear(self.api)
        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -100, -40, r)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -100, stackHeight, r, isQueued = 1)
        dType.SetEndEffectorSuctionCup(self.api, 1, 1)
        dType.SetWAITCmd(self.api, 2, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -100, -40, r, isQueued = 1)

        # dType.SetQueuedCmdStartExec(self.api)

        self.pieces -= 1

    def calibrate(self, stage):
        """ Calibrate robot and game with different stages """
        dType.SetQueuedCmdClear(self.api)

        if stage == 1:
            dType.SetWAITCmd(self.api, 0.1, 1)
            dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, 0, 50, 0, isQueued = 1)
            dType.SetHOMECmd(self.api, temp = 0, isQueued = 1)
            dType.SetQueuedCmdStartExec(self.api)
        elif stage == 2:
            dType.SetWAITCmd(self.api, 0.1, 1)
            dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, 50, -55, -40, isQueued = 1)
            dType.SetQueuedCmdStartExec(self.api)
        elif stage == 3:
            dType.SetWAITCmd(self.api, 0.1, 1)
            dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -55, -40, isQueued = 1)
            dType.SetQueuedCmdStartExec(self.api)

    def maxStack(self):
        """ TEST Max stack """
        dType.SetQueuedCmdClear(self.api)

        stackHeight = (self.pieces*3)+72
        r = -40

        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -40, r)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, stackHeight, r, isQueued = 1)
        dType.SetEndEffectorSuctionCup(self.api, 1, 1)
        dType.SetWAITCmd(self.api, 0.5, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 250, -50, -40, r, isQueued = 1)

    def moveAway(self):

        dType.SetWAITCmd(self.api, 0.1, 1)
        dType.SetPTPCmd(self.api, dType.PTPMode.PTPMOVLXYZMode, 50, -200, 50, 0, isQueued = 1)

    def disconnect(self):
        dType.DisconnectDobot(self.api)
