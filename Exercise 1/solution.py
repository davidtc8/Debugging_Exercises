############DEBUGGING#####################

# # Describe Problem
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it")

my_function()
#Problem: The function is not returning the print statement
#Solution: The issue is that the range function is not inclusive, therefore, when we're saying
#that you want range(1,20) it won't take into account the 20, therefore, you have to put from range(1,21) or lower the variable 'i'
