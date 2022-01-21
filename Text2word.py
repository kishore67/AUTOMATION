import pyautogui as p
import time as t

msg1 = open("kishore1.txt", "r") # reading the text file
msg = msg1.read()
t.sleep(5)

for i in msg:
    p.write(i) # writing the text file
