import os
import time

resize = 0
filename = '/home/pi/EncryptedFilesReceived/2018-12-09 18:27:18.txt'

sizeFile = os.stat(filename).st_size
if (sizeFile > 128):
	print(sizeFile)
	resize = sizeFile -128
	print (resize)
	
with open(filename, 'rb+') as filehandle:
	filehandle.seek(- resize, os.SEEK_END)
	filehandle.truncate()
	

		