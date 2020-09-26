from Tela1 import SetupTela1
from Tela2 import SetupTela2
from Tela3 import SetupTela3
from PosicaoTelas import Position

class OpenMultWin:
    def __init__(self):
        self.ST1 = SetupTela1()
        self.ST2 = SetupTela2()
        self.ST3 = SetupTela3()

    def Run(self):
        self.ST2.Run()
        self.ST1.Run()
        self.ST3.Run()


class PositionMultScreen:
    def __init__(self):
        self.Pos = Position()

    def Run(self):
        for i in range (3):
            if i == 0:
                self.Pos.Sent2First()
            if i == 1:
                self.Pos.Sent2Third()
            if i == 2:
                self.Pos.EnableExtension()
            self.Pos.openFullScreen()

OMW = OpenMultWin()
PMS = PositionMultScreen()
OMW.Run()
#PMS.Run()