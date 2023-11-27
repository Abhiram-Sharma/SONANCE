from Functions import *
x=True
Speak("Hey There")
Speak("I am Sonance Your Personal Desktop Assistant")
Speak("Try Giving Me a Command")
while x:
    query=listen("I am Listening, Command me")
    Speak(query)
    if "stop" in query.lower() or "quit"in query.lower():
        Speak("Thank you For Allowing Me to Assist, Always at your service")
        Speak("- Sonance...")
        x=False
    elif :
