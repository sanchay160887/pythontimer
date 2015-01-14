import Tkinter as tk
import sys
import time
from PIL import Image
from PIL import ImageGrab 
import time


def captureScreen():
    #time.sleep(1)
    timestr = time.strftime("%Y%m%d-%H%M%S")
    ImageGrab.grab().save(timestr+'.jpg', "JPEG")

def update_timeText():
    if (state):
        global timer

        timer[3] += 1
        
        
        if (timer[3] >= 100):
            captureScreen()
            timer[3] = 0
            timer[2] += 1
        
        if (timer[2] >= 60):
            timer[1] += 1
            timer[2] = 0

        if(timer[1]>=60):
            timer[0] += 1
            timer[1] = 0
            captureScreen()
        
        timeString = pattern.format(timer[0], timer[1], timer[2], timer[3])
        
        timeText.configure(text=timeString)
        
    root.after(10, update_timeText)


def start():
    global state
    state = True


def pause():
    global state
    state = False


def reset():
    global timer
    timer = [0, 0, 0, 0]
    timeText.configure(text='00:00:00:00')


def exist():
    root.destroy()


state = False

root = tk.Tk()
root.wm_title('Tracker Tool')


timer = [0, 0, 0, 0]

pattern = '{0:02d}:{1:02d}:{2:02d}:{3:02d}'


timeText = tk.Label(root, text="00:00:00:00", font=("Helvetica", 30))
timeText.pack()

startButton = tk.Button(root, text='Start', command=start)
startButton.pack()

pauseButton = tk.Button(root, text='Pause', command=pause)
pauseButton.pack()

resetButton = tk.Button(root, text='Reset', command=reset)
resetButton.pack()

quitButton = tk.Button(root, text='Quit', command=exist)
quitButton.pack()

update_timeText()
root.mainloop()