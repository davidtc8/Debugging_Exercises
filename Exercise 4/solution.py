############DEBUGGING#####################

# Describe Problem
# Fix the Errors
age = int(input("How old are you?: "))
if age >= 18:
    print(f"You can drive at age {age}.")
else:
    print(f"You can't drive when you're {age}")

#Solution:
# 1. There was no indentation
# 2. As we're putting an integer in the input statement, we need to put the 'int' statement before the function
# 3. there was no 'else' statement in case you are younger.
