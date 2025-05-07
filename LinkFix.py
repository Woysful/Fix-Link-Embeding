import pyperclip
import winsound
import requests
import sys

# Short link api
def tinyLink(str):
     api_url = f"https://tinyurl.com/api-create.php?url={str}"
     response = requests.get(api_url)
     return response.text

# Arguments check
if len(sys.argv) != 2:
    print("[ Wrong argument ]")
    sys.exit(1)
  
mode = sys.argv[1].lower()

# Link from clipboard
MyLink = pyperclip.paste()

# link editing
modified_link = MyLink.replace("twitter.com", "vxtwitter.com").replace("x.com", "vxtwitter.com").replace("bsky.app", "r.bskyx.app").replace("instagram.com", "ddinstagram.com")

# Argument check
if mode == "short":
    shortlink = tinyLink(modified_link)
    pyperclip.copy(shortlink)
elif mode == "raw":
    pyperclip.copy(modified_link)
else:
    sys.exit(1)

winsound.PlaySound(r'C:\Windows\Media\Speech On.wav', winsound.SND_FILENAME)