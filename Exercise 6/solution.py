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

#Solution: the append statement was at the end of the for loop and that's why it just gave us the last element of the list!
