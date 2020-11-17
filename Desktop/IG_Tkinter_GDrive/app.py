import tkinter
from instabot import Bot
from checkIMG import choose_option, image
from drive_list import image_input
from tkinter import Tk, Label, Button
import tkinter as tk
from PIL import ImageTk,Image
import time



bot = Bot()

choose_option()
#get picture data from main choosing img function
# if not image:
#     picture = ''.join(choose_img)
# else:
#     picture = ''.join(image)
time.sleep(3)
if str(image) != '':
    picture = ''.join(image)
elif str(image_input) != '':
    picture = ''.join(image_input)


###TKINTER GUI###
class IGGUI(tk.Frame):
    #set master to none 
    def __init__(self, master=None):
        #give access to methods and propertie of parent or siblings
        super().__init__(master)
        self.master = master
        #self.img = ImageTk.PhotoImage(Image.open(picture))
        self.image = Image.open(picture)
        #resize the image 
        self.image = self.image.resize((250,200), Image.ANTIALIAS)
        #add the image to the GUI
        self.img = ImageTk.PhotoImage(self.image)
        self.create_widgets()
    
    #create/assign the layout of Tkinter GUI 
    def create_widgets(self):
        self.photo = Label(image=self.img)
        self.photo.grid(row=0, column=0)

        self.label = Label(text="Type the text for IG post")
        self.label.grid(row=1,column=0)

        #save the string content in the self.content variable
        self.content = tkinter.StringVar()
        self.e1 = tkinter.Entry(width=25, textvariable = self.content)
        self.e1.grid(row=2, column=0)

        #on button click run the callback function
        self.button = Button(text="Submit", command=self.callback)
        self.button.grid(row=3, column=0)
        

    #get the self.content text content assign it to value variable destroy the GUI thenafter and global assign the value to entry_text
    def callback(self):
        value = self.content.get()
        self.master.destroy()

        global entry_text 

        entry_text = value


#create tkinter instance and initialize the interpreter
root = tkinter.Tk()
#assign it to the IGGUI class 
app = IGGUI(master=root)
#run the event loop
app.mainloop()


###Executing the post with choosen file###
bot.login(username='unlimited_testing', password='Asebomu12')

text = app.callback
bot.upload_photo(picture, caption=entry_text)




