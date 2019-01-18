import glob, os

def oldest():
        os.chdir("/home/pi/Desktop/temp/test/client/data")
	oldest = min(glob.iglob('*.txt'), key = os.path.getctime) 
	print(oldest)
	return oldest
	


