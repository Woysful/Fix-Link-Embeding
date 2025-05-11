import pyperclip, requests, winsound, sys

def tinyLink(str):
    api_url = f"https://tinyurl.com/api-create.php?url={str}"
    response = requests.get(api_url)
    return response.text

def run(arg):

    MyLink = pyperclip.paste()

    replacements = {
    "twitter.com": "vxtwitter.com",
    "x.com": "vxtwitter.com",
    "bsky.app": "r.bskyx.app",
    "instagram.com": "ddinstagram.com"
    }

    Fixed_Link = MyLink
    for old, new in replacements.items():
        if old in MyLink:
            Fixed_Link = MyLink.replace(old, new)
            break

    match arg:
        case "short":
            shortlink = tinyLink(Fixed_Link)
            pyperclip.copy(shortlink)
        case "long":
            pyperclip.copy(Fixed_Link)
        case "tiny":
            MyLink = tinyLink(MyLink)
            pyperclip.copy(MyLink)
        case _:
            sys.exit(1)

    winsound.PlaySound(r'.\sound\done.wav', winsound.SND_FILENAME)
    sys.exit(1)
