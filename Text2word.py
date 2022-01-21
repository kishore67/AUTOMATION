import pyautogui as p
import time as t

msg1 = open("kishore1.txt", "r") # read the text file
msg = msg1.read()
t.sleep(5)

p.press('win') # press windows key
t.sleep(1)
p.write('msword') #search msword
t.sleep(2)
p.press('enter')

t.sleep(2)
p.press("enter")

for i in msg:
    p.write(i) # write the readed text file content in the ms word
