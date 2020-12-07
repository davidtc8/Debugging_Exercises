############DEBUGGING#####################

# Describe Problem

# Play Computer
year = int(input("What's your year of birth?: "))
if year > 1980 and year < 1994:
    print("You are a millenial.")
elif year >= 1994:
    print("You are a Gen Z.")

#Solution: The indentation was wrong! In Python there should be indentation
#Also, when you run 1994 it didn't run, that's because of the parameters, we have to put '>=' sign
