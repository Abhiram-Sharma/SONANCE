from Functions import *
x=True
Speak("Hey There")
Speak("I am Sonance Your Personal Desktop Assistant")
Speak("Try Giving Me a Command")
n=0
while x:
    query=listen("").lower()
    Speak(query)
    if "stop" in query or "quit"in query:
        Speak("Thank you For Allowing Me to Assist, Always at your service")
        Speak("- Sonance...")
        x=False
    elif "photo" in query:
        capture_photo(n)
        n+=1
        pass
    elif "message" in query:
        Speak(telemsg(listen("Tell Me Your Message")))
        pass
    elif "youtube" in query:
        Speak(YoutubeSearch(listen("What would you want to search in youtube")))
        pass
    elif "song" in query:
        Speak(spotify(listen("which song shall I search")))
        pass
    elif "command" in query or "prompt" in query:
        cmdpmt()
        pass
    elif "screenshot" in query or "shot" in query:
        Speak(take_screenshot(n))
        n+=1
        pass
    elif "anime" in query:
        Speak(anime(listen("Which anime would you like to search")))
        pass
    elif "todo" in query or "to" in query or "do" in query:
        query_todo=listen("Do you want to Add todo, View Todo, or delete todo").lower()
        if "add" in query_todo:
            Speak(addtodo(listen("What is the Task")))
        elif "view" in query_todo:
            Speak(viewtodo())
        elif "delete" in query_todo or "remove" in query_todo:
            Speak(deletetodo(listen("Which todo to remove")))
        else:
            Speak("Sorry could not understand what you wanted to do with todo list")
        pass
    elif "google" in query:
        Speak(gs(listen("What do you want to search for")))
        pass
    elif "Not Recognizable" not in query:
        Speak(gpt(query))
        pass
    else:
        pass

