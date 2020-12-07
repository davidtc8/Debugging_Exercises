############DEBUGGING#####################

#Describe Problem
#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Solution: In the variable word_per_page there was a '==' signs that diddn't let us run the program correctly!
