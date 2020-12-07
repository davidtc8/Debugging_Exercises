############DEBUGGING#####################

# Describe Problem
#Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
    b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])

#Issue: The issue it that the code returns a string, instead of multiplyin each variable * 2 in the 'mutate' list!
