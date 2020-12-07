############DEBUGGING#####################

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)
print(dice_imgs[dice_num])

#Solution: The randint was in a range from 1-6, but this is incorrect, because, when we're
#talking about a list in Python, in this case goes from 0-5, not 1-6, that's why when we
#ran the program, when the random number was 6, it was gonna be a problem, because it
#was out of the range of the python list 'dice_imgs'
