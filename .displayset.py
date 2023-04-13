from os import system
from sys import exit

def readoutput(filename):
	f = open(filename, "r")
	out = f.read() 
	f.close()
	return out

def sendoutput(command, filename):
	system(f"{command} > {filename}")

# First run command
sendoutput("xrandr", "display.txt")
if "VGA" in readoutput("display.txt"):
	system("xrandr --output LVDS --off")
	exit()
else:
	exit()
