import webbrowser

def YoutubeSearch(txt):
    que=f"https://www.youtube.com/results?search_query={txt}"
    webbrowser.open(que)
    return "Top results are displayed on your browser"
