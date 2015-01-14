import Tkinter as tk
import sys
import time
from PIL import Image
from PIL import ImageGrab 
from email.MIMEText import MIMEText
import time
global state 
state = False

root = tk.Tk()
root.mainloop()

def captureScreen():
    #time.sleep(1)
    timestr = time.strftime("%Y%m%d-%H%M%S");
    ImageGrab.grab().save(timestr+'.jpg', "JPEG");
	

def update_timeText():
	print "CAlLED"
    while(state):
		print time.time() ;
		time.sleep(1);
		# timeString = pattern.format(timer[0], timer[1], timer[2], timer[3])
		# timeText.configure(text=timeString)
		captureScreen();
		
		root.after(1, update_timeText)

def start():
    state = True;


def pause():
	state = False;


def reset():
    timer = [0, 0, 0, 0];
    timeText.configure(text='00:00:00:00');


def exist():
    root.destroy();


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

