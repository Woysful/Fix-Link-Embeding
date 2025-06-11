from pyperclip  import paste
from re         import compile

url = paste().strip()

def url_valid():
    url_pattern = compile(
    r'((http[s]?://)?(www\.)?'
    r'([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}'
    r'(/[^\s]*)?)')
    if not url_pattern.match(url):
        return False, url
    else:
        return True, url