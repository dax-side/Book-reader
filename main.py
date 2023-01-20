# Audio Story Book
# Harvarx CS50 Final Project December 2020
# Software designed by Sangwani Peter Zyambo

import pyttsx3
import PyPDF2

book = open('short_stories_for_children.pdf', 'rb')# open the book
pdfReader = PyPDF2.PdfFileReader(book)# Read from a book
pages = pdfReader.numPages

print(" press 0 for Story Titles")
print ('Choose Story Number (1 -17)')
story = int(input("Enter choice: "))

# Function to stories from the book
def story_reader():
    page = pdfReader.getPage(num) #
    #print(page) # Printing the numbr os pages in the book
    text = page.extractText()

    reader = pyttsx3.init()  # creating reader object
    #engine properties
    reader.setProperty('rate', 125) #voice rate
    reader.say(text)
    reader.runAndWait()
    reader.stop()

# Showing a list of stories in the book
if story == 0:
    with open('list.pdf', 'rb') as list: #text file with stories
        pdfReader = PyPDF2.PdfFileReader(list)# Read from a book
        pages = pdfReader.numPages
        page = pdfReader.getPage(0)
        text = page.extractText()
        engine = pyttsx3.init()  # creating reader object
        engine.say(text)
        engine.runAndWait()
        engine.stop()

#Reading story 1
elif story == 1:
    print('Man Overboad')
    for num in range(4,12):
       story_reader()

#Reading story 2
elif story == 2:
    print('When Papa Scolded Me')
    for num in range(13, 18):
       story_reader()

#Reading story 3
elif story == 3:
    print('To The Memory Of A Lion')
    for num in range(19, 27):
       story_reader()

#Reading story 4
elif story == 4:
    print('The Triumphant Smile')
    for num in range(28, 31):
       story_reader()

#Reading story 5
elif story == 5:
    print('The Turkisk Cap')
    for num in range(32, 37):
       story_reader()

#Reading story 6
elif story == 6:
    print('The Goose Thieves')
    for num in range(38, 45):
       story_reader()

#Reading story 7
elif story == 7:
    print('Christmas Bells')
    for num in range(46,53):
        story_reader()

#Reading story 8
elif story == 8:
    print('In The Guava Orchad')
    for num in range(54,59):
        story_reader()

#Reading story 9
elif story == 9:
    print('All Because of My Hair')
    for num in range(60,64):
        story_reader()

#Reading story 10
elif story == 10:
    print('The Pink Card')
    for num in range(65,73):
        story_reader()

#Reading story 11
elif story == 11:
    print('The Unforgettable Journey')
    for num in range(74,80):
        story_reader()

#Reading story 12
elif story == 12:
    print("Varukanka's Lemonade Pals")
    for num in range(81,89):
        story_reader()

#Reading story 13
elif story == 13:
    print('Hanuman And I')
    for num in range(90,94):
        story_reader()

#Reading story 14
elif story == 14:
    print('At The Party')
    for num in range(95,99):
        story_reader()

#Reading story 15
elif story == 15:
    print('Outwitted I')
    for num  in range(100,104):
        story_reader()

#Reading story 16
elif story == 16:
    print('That Sunday Morning')
    for num in range(105,108):
        story_reader()

#Reading story 17
elif story == 17:
    print('The Boy From Standard III')
    for num in range(109,114):
        story_reader()
