# Importing all the necessary modules
from tkinter import *
from tkinter.messagebox import showinfo
import pyttsx3

# Creating the python text to speech and speech to text functions
def speak(text: str):
    engine = pyttsx3.init()
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 100)
    engine.say(text)
    engine.runAndWait()

#-----we initialise the pyttsx3 library and store it in the variable called engine.
#-----we use the .setProperty() method to set the properties ‘rate’ and ‘volume’ of the voice to 10 and 100 respectively.
#-----we use the .say() method and provide it with the text taken as the argument to speak the said text.
#-----We use the .runAndWait() method to tell the engine that the words spoken should not collide with any other task to be executed or is being executed.


    
# Creating the main TTS function 
def TTS():
    tts_wn = Toplevel(root)
    tts_wn.title('Text-To-Speech Converter')
    tts_wn.geometry("300x300")
    tts_wn.configure(bg='lightgrey')
    
    Label(tts_wn, text='Text-To-Speech Converter', font=("Comic Sans MS", 15), bg='lightgrey').place(x=20)
    
    text = Text(tts_wn, height=8, width=31, font=12)
    text.place(x=8, y=60)
    
    speak_btn = Button(tts_wn, text='LISTEN', bg='royalblue', command=lambda: speak(str(text.get(1.0, END))))
    speak_btn.place(x=130, y=230)

#------The Toplevel widget is used to create a window on the top of the windows present. 
#------label means a title  we called it "Text to speech"(not important)
#------we use text , to make the user input the word that he want to listen to it
#------speak_btn , its a buttom ot press it to listen . we insert on it the text that added to read it    

    

# Creating the main GUI window
root = Tk()
root.title('Python Project Text_To_Speech')
root.geometry('300x300')
root.resizable(0, 0)
root.configure(bg='lightgrey')

#-------The Tk() class is used to initialize the python text to speech project window
#-------The .title() method is used to specify a title of the window.
#-------The .geometry() method is used to set the initial geometry, the initial dimensions of the window.
#-------The .resizable() decides whether the user will be allowed to resize the window after initialization or not.
#-------The .configure() method is used to configure certain properties of the window in the form of arguments of this method




# Placing all the components
Label(root, text='Python Project Text_To_Speech',
      font=('Comic Sans MS', 16), bg='lightgrey', wrap=True, wraplength=300).place(x=65, y=40)

tts_btn = Button(root, text='TTS Conversion', font=('Helvetica', 14), bg='royalblue', command=TTS)
tts_btn.place(x=75, y=180)

#------The master, text, bg, and font attributes are the same as in the Label class.
#------The command attribute is used to define the function that the button will execute when it is pressed.





# Updating main window
root.update()
root.mainloop()

#-------The .update() and .mainloop() methods of the Tk() class are used to put the window in a loop such
#                                     that it does not get destroyed the moment it appears on the screen.
