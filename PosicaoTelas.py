import pyautogui, time

class Position:
    def __init__(self):
        pass

    def EnableExtension(self):
        pyautogui.moveTo(x=1803, y=50, duration=0.25)
        pyautogui.click(x=1803, y=50)

    def Sent2First(self):
        time.sleep(2)
        pyautogui.moveTo(x=1759,y=15, duration=0.5)
        pyautogui.dragTo(x=-960,y=100,duration=2.0)

    def Sent2Third(self):
        self.EnableExtension()
        time.sleep(2)
        pyautogui.moveTo(x=1759,y=15, duration=0.5)
        pyautogui.dragTo(x=2880,y=100,duration=2.0)

    def openFullScreen(self):
        pyautogui.press('F11')
