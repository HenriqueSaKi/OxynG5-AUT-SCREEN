import pyautogui, time

class Position:
    def __init__(self):
        pass

    def EnableExtension(self):
        pyautogui.click(x=1780, y=50)

    def Sent2First(self):
        self.EnableExtension()
        time.sleep(2)
        pyautogui.moveTo(x=1775,y=15)
        pyautogui.dragTo(x=-960,y=100,duration=2.0)

    def Sent2Third(self):
        self.EnableExtension()
        time.sleep(2)
        pyautogui.moveTo(x=1775,y=15)
        pyautogui.dragTo(x=2880,y=100,duration=2.0)

    def openFullScreen(self):
        pyautogui.press('F11')
