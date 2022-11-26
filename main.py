import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command_v1 = listener.recognize_google(voice)
            command_v1 = command_v1.lower()
            if 'alexa' in command_v1:
                command_v1 = command_v1.replace('alexa', '')
                print(command_v1)
    except:
        pass
    return command_v1


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "where is room 209" in command:
        room_209 = "Room 209 is in the new building," \
                   " you walk in, turn right, " \
                   "go up stairs, " \
                   "and when you are up stairs, " \
                   "you go left walk, " \
                   "all the way down the hall, " \
                   "and it is the last classroom on the left." \
                   " The teacher is Magali"
        print(room_209)
        talk(room_209)
    elif "where is the design room" in command:
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
    else:
        talk('Please say the command again.')


while True:
    run_alexa()