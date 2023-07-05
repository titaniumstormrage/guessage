'''
This program came to be as a joke on a twitch stream (https://www.twitch.tv/claradactyl).
On that stream there's a command called !guessage which basically "guesses" Claras age
We tried to get the age 1337 but we had to give up since it disrupted the stream
I didn't want to give up so I wrote this little thing
Later on (just before pushing it onto github) I also wrote it a GUI
(I know my code is pretty lousy here but meh it's 3am rn so frankly I don't care)
Also anyone that sees this can use this code as they see fit I don't really care how people use this one.
'''
#Importing the modules
from time import perf_counter, sleep
from random import seed, randint
from tkinter import Tk, Label, Button, END
import tkinter.scrolledtext as tkst

#Inserts the results of "guessage" into the "scrollbox"
def scrollbox_insert(message):
        scrollbox.configure(state='normal')
        scrollbox.insert(END, message + '\n')
        scrollbox.configure(state='disabled')
        scrollbox.yview(END)
        root.update()    

#Generates the age
def guessage():
        seed()
        years = 0
        age = 0
        lines = 0

        #Times the amount of time it takes to run the search for truth
        start_time = perf_counter()

        #Disables the button so the user can't mess with the end statistics
        start_button.configure(state='disabled')
        
        while age == 0:
                sleep(0.01)
                #Generates the years
                if years != 1337:
                        years = randint(1, 9999)
                        scrollbox_insert(f"I guess Clara is {years} years old?")
                        lines = lines + 1
                #If desired year is achived prints the total of years needed to reach that point
                else:
                        scrollbox_insert(f"It took {lines} tries to get the legendary age!")
                        scrollbox_insert(f"Time: {perf_counter() - start_time} seconds!")
                        age = 1

        #Enables the button again
        start_button.configure(state='normal')
                        

#Generates the GUI
root = Tk()
root.title("G U E S S   A G E !")
root.geometry("800x210")
root.resizable(0, 0)

#Text
label = Label(root, text="This wonderful program was designed with one goal in mind! To find the legendary age of the one, the only, timeless Claradactyl!")
label.pack()

#The logbox basically
scrollbox = tkst.ScrolledText(root, width  = 120, height = 10)
scrollbox.pack()

#The button
start_button = Button(root, text="Letsa go!", command=guessage)
start_button.pack()


root.mainloop()


#From what I've gathered Clara can actually code a bit (or at least tried learning it)
#In that case I wonder if she'll actually read this...
#If you read this Clara then hi!
                
