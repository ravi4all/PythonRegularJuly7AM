from datetime import datetime as dt
import os, random, glob

print("How may I assist you ?")

helloIntent = ["hi", "hello", "hi there", "hey", "hello there", "hey there"]
dateIntent = ["date","tell me date","what's the date","please tell me date","what's the date today"]
timeIntent = ["time","tell me time","what's the time","please tell me time","what's the time now"]
musicIntent = ["song","play song","play music"]

# Logical Operator - and, or, not
# Membership Operators - in, not
# Identity Operators - is is not

while msg := input("Enter your message : "):
    if msg in helloIntent:
        print("Hello User")
    elif msg in dateIntent:
        current_date = dt.now().date()
        print(current_date.strftime("%a, %d %b, %Y"))
    elif msg in timeIntent:
        current_time = dt.now().time()
        print(current_time.strftime("%H:%M:%S, %p"))
    elif msg in musicIntent:
        os.chdir(r"C:\Users\ASUS PC\Music")
        songs = glob.glob("*.mp3")
        song = random.choice(songs)
        os.startfile(song)
    elif msg == "show songs":
        pass
    elif msg == "bye":
        print("Hello User")
        break
    else:
        print("I don't understand")
