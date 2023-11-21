import webbrowser
def ott(stxt):
    txt='+'.join(stxt.split())
    url=f'https://animension.to/search?search_text={txt}'
    webbrowser.open(url)
    return "search result has been displayed"
