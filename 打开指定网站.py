import webbrowser

def open_website(url):
    """
    Open a website in the default browser.
    Args:
        url: str. The URL of the website to open.
    """
    webbrowser.open_new_tab(url)

# open Google in the default browser
open_website('https://www.google.com')

# open Baidu in the default browser
open_website('https://www.youtube.com')
