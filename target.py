#GET AB CONFIG FILE
import os
import sys
from config import TARGET_SLOT

#UPDATE CONFIG FILE FUNCTION
def updateAB(fileName, originalText, newText):
	f = open(fileName,'r')
	filedata = f.read()
	f.close()

	newdata = filedata.replace(originalText, newText)

	f = open(fileName,'w')
	f.write(newdata)
	f.close()
	return
 

if __name__ == '__main__':
	#DID WE GET A SLOT # IN THE COMMAND?
	if sys.argv[1]:
		NEWSLOT = sys.argv[1]
	else:
		#OUTPUT AND ASK QUESTION
		print("++++++++")
		print("Current TARGET_SLOT: ") 
		print(TARGET_SLOT)
		print("++++++++")
		NEWSLOT = input("Enter new SLOT TARGET: ")

	# EDIT AUTOBIDDER CONFIG FILE
	
	ORIG_TARGET = "TARGET_SLOT = "+str(TARGET_SLOT)
	NEW_TARGET = "TARGET_SLOT = "+str(NEWSLOT)
	updateAB("../harmony_autobidder/config.py",ORIG_TARGET,NEW_TARGET)
	print("++++++++")
	print("Target slot updated to "+NEWSLOT)
	print("++++++++")
	os.system("tmux kill-ses -t autobidder")
	os.system("tmux new-session -s autobidder 'python3 ~/harmony_autobidder/autobid.py'")