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









# import numpy as np
#
# size = int(input("enter the first array size:"))
# arr_1 = []
# arr_2 = []
# for x in range(size):
#     arr_1.append([int(y) for y in input("enter the elements with seprate single space:").split()])
#
# print(arr_1)
#
# size1 = int(input("enter the second array size:"))
#
# for z in range(size1):
#     arr_2.append([int(s) for s in input("enter the elements with seprate single space:").split()])
#
# print(arr_2)
#
# np_ar1 = np.array(arr_1)
# np_ar2 = np.array(arr_2)
#
# print(np_ar1 + np_ar2)
#
#
# # array1 = np.array(li1,dtype=int)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # import pywhatkit
# # import pyautogui
#
# # i = 0
# # while i < 5:
# #     print(i,end=" ")
# #     i += 1
# #     if i == 3:
# #         break
# #     else:
# #         print(0)
#
# # tup =(0,1,2,3)
# # print(tup[::-1])
#
#
#
#
#
#
#
#
#
#
#
# # # def kishore(name1,age1):
# # #     # name=input("enter a name:")# declare a variable for user name by input
# # #     print(name1)
# # #     # age=int(input("enter a age:"))# declare a variable for user age by input
# # #     if age1>18: # check the age greater than 18 or not
# # #         print("eligable for vote")
# # #     else:
# # #         print("not eligable for vote",age1)
# # #
# # #
# # # def right_angle(num):
# # #     for i in range(num):
# # #         for j in range(i + 1):
# # #             print(" * ", end="")
# # #         print()
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# #
# # # kishore("kishore",19)
# #
# # # first_num = int(input("enter the number you want to skip:"))
# # # second_num =int(input("enter the range of the iteration:"))
# # # first_num =2
# # # second_num=20
# #
# # # for i in range(second_num):
# # #     # if i % 10 == first_num:
# # #     if i % first_num==0:
# # #         continue
# # #     print(i)
# # #
# # # for i in range(second_num):
# # #     if i % 10 !=2:
# # #         print(i)
# #
# # num = int(input("enter the number:"))
# # for i in range(num):
# #     # for j in range(i+1): #right angle triangle
# #     # for j in range(num):   # square
# #     # for j in range(num-i): # revesed right angle triangle
# #     for a in range(num):
# #         print(end=" ")
# #     for j in range(i):
# #         print(" * ",end="")
# #     print()
