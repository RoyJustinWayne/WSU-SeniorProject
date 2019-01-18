#!/usr/bin/python

import time 


counter = 0;
while counter < 100:
    print("Hello World");
    time.sleep(3);
    counter += 1;
    f = open("/home/pi/testpy.txt","a");
    f.write("Hello World\n");
    f.close(); 
 