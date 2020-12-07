############DEBUGGING#####################

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

#Issue: When you run the code a couple of times, for some reason it produces the following error:

#Error:
#Traceback (most recent call last):
  #File "filelocation", line 7, in <module>
    #print(dice_imgs[dice_num])
#IndexError: list index out of range
