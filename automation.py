import pyautogui as p, time as t

#this code is used to automate Whats app messages using python

p.press('win')
t.sleep(1)
p.write('chrome')
t.sleep(2)
p.press('enter')

t.sleep(10)
p.hotkey('ctrl','f')
p.write('spanning tree in maths')
t.sleep(2)
p.press('enter')

t.sleep(5)
msg=["1", "2", "3", "4", "kishore kishore kishore kishore kishore"]

for i in msg:
    p.write(i)
    p.press('enter')
    t.sleep(1)

