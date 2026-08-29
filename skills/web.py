import webbrowser
from urllib.parse import quote_plus


def open_website(url, name):
    try:
        webbrowser.open(url)
        return f"Opening {name}."

    except Exception as error:
        print(f"Web error: {error}")
        return f"Sorry, I could not open {name}."


def open_google():
    return open_website(
        "https://www.google.com",
        "Google"
    )


def open_youtube():
    return open_website(
        "https://www.youtube.com",
        "YouTube"
    )


def open_github():
    return open_website(
        "https://github.com",
        "GitHub"
    )


def google_search(query):

    if not query:
        return "Please tell me what you want me to search for."

    search_url = (
        "https://www.google.com/search?q="
        + quote_plus(query)
    )

    webbrowser.open(search_url)

    return f"Searching Google for {query}."


def youtube_search(query):

    if not query:
        return "Please tell me what you want me to search for."

    search_url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(query)
    )

    webbrowser.open(search_url)

    return f"Searching YouTube for {query}."