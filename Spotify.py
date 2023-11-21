import webbrowser
def spotify(txt):
    url=f'https://open.spotify.com/search/{txt}'
    webbrowser.open(url)
    return "search result has been displayed"
