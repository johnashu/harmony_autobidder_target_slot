#GET AB CONFIG FILE
import os
import sys
sys.path.insert(0, '../harmony_autobidder')
from config import TARGET_SLOT

#UPDATE CONFI FILE FUNCTION
def updateAB(fileName, originalText, newText):
	f = open(fileName,'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace(originalText, newText)

	f = open(fileName,'w')
	f.write(newdata)
	f.close()
	return
	

#OUTPUT AND ASK QUESTION
print("Current TARGET_SLOT: ")	
print(TARGET_SLOT)
print("++++++++")
NEWSLOT = input("Enter new SLOT TARGET: ")

# EDIT AUTOBIDDER CONGIF FILE
ORIG_TARGET = "TARGET_SLOT = "+str(TARGET_SLOT)
NEW_TARGET = "TARGET_SLOT = "+str(NEWSLOT)
updateAB("../harmony_autobidder/config.py",ORIG_TARGET,NEW_TARGET)
print("++++++++")
print("Target slot updated to "+NEWSLOT)

cmd = 'tmux a'
os.system(cmd)