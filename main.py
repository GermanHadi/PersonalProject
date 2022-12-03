import speech_recognition as sr
import pyttsx3
import pywhatkit
import webbrowser
import datetime
from tkinter import *
import wikipedia
import pyjokes


ear_alexa = sr.Recognizer()
engine_alexa = pyttsx3.init()
voices = engine_alexa.getProperty('voices')
engine_alexa.setProperty('voice', voices[1].id)


def talk(text):
    engine_alexa.say(text)
    engine_alexa.runAndWait()

def use_mic():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = ear_alexa.listen(source)
            command_v1 = ear_alexa.recognize_google(voice)
            command_v1 = command_v1.lower()
            if 'alexa' in command_v1:
                command_v1 = command_v1.replace('alexa', '')
                print(command_v1)
    except:
        pass
    return command_v1



def run_islkdirect():
        command = use_mic()
        print(command)
        if 'shush' in command:
            talk("say nothin boss")
            command = False
        elif 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)

        elif "good bye" in command or "ok bye" in command or "stop" in command:
            talk('Your personal assistant is shutting down, Good bye')
            screen.destroy()

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'brother who is' in command:
            person = command.replace('brother who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)

        elif 'run me joke' in command:
            talk(pyjokes.get_joke())

        elif "where is room 209" in command:
            room_209 = "Room 209 is in the new building," \
                       " you walk in, turn right, " \
                       "go up stairs, " \
                       "and when you are up stairs, " \
                       "you go walk left , " \
                       "all the way down the hall, " \
                       "and it is the last classroom on the left." \
                       " The teacher is Magali"
            print(room_209)
            talk(room_209)

        elif "fam where is the design room" in command:
            design_room ="The design room is in the old building, " \
                         "on the right of the flag, " \
                         "when you enter the old building you go down the stairs, " \
                         "to the basement," \
                         " turn right," \
                         " go all the way down the hallway and the classroom is," \
                         " on the right." \
                         " The teacher is Adriaan "
            print(design_room)
            talk(design_room)

        elif "where is room 142" in command:
            room_142 = "Room 142 is in the old building, " \
                       "on the right of the flag, " \
                       "when you enter the old building, " \
                       "you go up the stairs," \
                       " onto the second floor," \
                       " turn left," \
                       " when up the stairs," \
                       " go straight until the end of the hallway," \
                       " and turn left," \
                       " go straight until you see the big doors," \
                       " there should be stairs on the left," \
                       " but go through the other big door," \
                       " and its the classroom on the left." \
                       "The teacher is James"
            print(room_142)
            talk(room_142)

        elif "where is room 129" in command:
            room_129 = "Room 129 is is in the old building," \
                       " on the right of the flag," \
                       " when you enter the old building," \
                       " you go up the stairs," \
                       " onto the second floor," \
                       " turn left," \
                       " when up the stairs," \
                       " go straight until you see the group room," \
                       " on the left," \
                       " and on the right of the group room you will see room 129." \
                       " The teacher is Jaryn"
            print(room_129)
            talk(room_129)

        elif "where is room 233" in command:
            room_233 = "Room 233 is in the new building," \
                       " you walk in," \
                       " turn right," \
                       " go up stairs," \
                       " and when you are up stairs," \
                       " you turn right," \
                       " and walk forward until you see the first classroom," \
                       " on the right." \
                       " The teacher is Lindsay "
            print(room_233)
            talk(room_233)

        elif "where is room 218" in command:
            room_218 = "Room 218 is in the new building," \
                       " you walk in," \
                       " turn right," \
                       " go up stairs," \
                       " and when you are up stairs," \
                       " on the left of the toilets you will see a classroom," \
                       " the first classroom," \
                       " on the right of the hallway." \
                       " The teacher is Alex "
            print(room_218)
            talk(room_218)

        elif "where is the PE hall" in command:
            PE_Hall = "The PE hall is the building 12:00," \
                      " to where you lock your bike," \
                      " you walk straight," \
                      " passing the new and old building," \
                      " until you reach the PE Hall. " \
                      "The teacher is Vlad"
            print(PE_Hall)
            talk(PE_Hall)

        elif "where is room 207" in command:
            room_207 = "Room 207 is is in the new building," \
                       " you walk in," \
                       " turn right," \
                       " go up stairs," \
                       " and when you are up stairs," \
                       " you go left walk," \
                       " until you reach the door," \
                       " the classroom is on the left of the doors."
            print(room_207)
            talk(room_207)

        elif "open google" in command:
            webbrowser.open_new_tab("https://www.google.com")
            talk("ok! ok! google is openin chill.")


        elif "open gmail" in command:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/?tab=wm#inbox")
            talk("say nothing gmail is now open fam")


        elif "open spotify" in command:
            webbrowser.open_new_tab("https://open.spotify.com/")
            talk("calm down it's runnin")


        elif "open managebac" in command:
            webbrowser.open_new_tab("https://www.managebac.com/")
            talk("don't worry fam managebac is open bruv")


        else:
                talk('Please say the command again.')
        return

def info():

  info_screen = Toplevel(screen)
  info_screen.title("Info")
  info_screen.iconbitmap()


  creator_label = Label(info_screen,text = "Created by Hadi Paul Scharbrodt")
  creator_label.pack()

  Age_label = Label(info_screen, text= " at the age of 15")
  Age_label.pack()


def select():

  select_screen = Toplevel(screen)
  select_screen.title("Select")
  select_screen.iconbitmap()

def commands():

  commands_screen = Toplevel(screen)
  commands_screen.title("Commands")
  commands_screen.iconbitmap()

  command_1_label = Label(commands_screen,text = "Ask For Rooms")
  command_1_label.pack()

  command_2_label = Label(commands_screen, text= " Ask The Time")
  command_2_label.pack()

  command_3_label = Label(commands_screen, text= " Who Someone Is On Wiki")
  command_3_label.pack()

  command_4_label = Label(commands_screen, text= "Play A Song On Youtube")
  command_4_label.pack()

  command_5_label = Label(commands_screen, text= " Open "
                                                 "Google, "
                                                 "Gmail, "
                                                 "Managbac"
                                                 " and Spotify")
  command_5_label.pack()

  command_6_label = Label(commands_screen, text= " Ask To Tell A Joke")
  command_6_label.pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("700x800")


    name_label = Label(text="ISLK Direct", width=300, bg="black", fg="white", font=("Times New Roman", 13))
    name_label.pack()

    info_button = Button(text="Info", command=info)
    info_button.pack(pady=10)

    select_button = Button(text="Click Me", command=screen.destroy)
    select_button.pack(pady=20)

    commands_button = Button(text="Commands", command=commands)
    commands_button.pack(pady=30)

    screen.mainloop()

main_screen()

while True:
    run_islkdirect()

