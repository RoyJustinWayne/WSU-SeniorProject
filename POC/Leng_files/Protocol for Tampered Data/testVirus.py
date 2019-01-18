
import random 


f = open(r"C:\Users\lengl\Desktop\testBinary.txt",'a')
f.truncate()
for i in range(10000):
    rand = random.choice("abcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*()_+")
    f.write(rand)
f.close()


