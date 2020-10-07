from Tela2 import SetupTela2 as ST2
from Tela1 import SetupTela1 as ST1
from Tela3 import SetupTela3 as ST3
from PosicaoTelas import Position as Pos
import time


class PositionMultScreen:
    def __init__(self):
        pass

    def Run(self):
        time.sleep(2)
        for i in range (3):
            if i == 0:
                Pos().Sent2Third()
                time.sleep(1)
                ST3().MaxWindow()
            if i == 1:
                Pos().Sent2First()
                time.sleep(1)
                ST1().MaxWindow()
            if i == 2:
                Pos().EnableExtension()
            Pos().openFullScreen()
            time.sleep(2)

PMS = PositionMultScreen()
PMS.Run()
