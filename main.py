# pip install pyttsx3 --> pyttsx3 is the text to speech engine for python....it works offline
import pyttsx3 # importing the pyttsx3 module

engine=pyttsx3.init() # initializing the python text to speech engine
voices=engine.getProperty("voices") # get list of all the voices that the engine can have
engine.setProperty("voice",voices[1].id) # set a voice for the engine
                                         # 1--> female voice , 2--> male voice


def say(sentence):      # this is the function that tells the computer to say the sentence
    engine.say(sentence) # say the sentence
    engine.runAndWait() # wait till the sentence is said completely

path_file = r"E:\book.txt" # this is the path of the text file, replace it with your own path
file=open(path_file,'r') # open the file
while(True): # starting an infinite loop
    line=file.readline() # readine lines from the text file one by one
    if(line==''): # if no text is found, that means we have reached the end of text file
        break # break the infinite loop
    else: # if we got any text , then we will make the computer say it
        say(line) # make the computer say the line
file.close() # close the file after the reading is complete