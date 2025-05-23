import webbrowser

def handle(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching web for {query}"