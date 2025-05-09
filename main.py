import sys,os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

import pyperclip, requests, winsound
from flowlauncher import FlowLauncher

class LinkFix(FlowLauncher):
    def query(self, query):   
        buttons = [
            {
                "Title": "Fixed Link | Tiny",
                "SubTitle": "Fix + Makes your link tiny (it could take a few seconds)",
                "IcoPath": "Images\\FixedTiny.png",
                "JsonRPCAction": {
                    "method": "run_fix",
                    "parameters": ["short"],
                    "dontHideAfterAction": False
                }
            },
            {
                "Title": "Fixed Link",
                "SubTitle": "Fixes your link",
                "IcoPath": "Images\\Fixed.png",
                "JsonRPCAction": {
                    "method": "run_fix",
                    "parameters": ["long"],
                    "dontHideAfterAction": False
                }
            },
            {
                "Title": "Tiny Link",
                "SubTitle": "Just makes your link tiny (it could take a few seconds)",
                "IcoPath": "Images\\TinyLink.png",
                "JsonRPCAction": {
                    "method": "run_fix",
                    "parameters": ["tiny"],
                    "dontHideAfterAction": False
                }
            }
        ]
        return buttons

    def run_fix(self, mode):
        def tinyLink(str):
            api_url = f"https://tinyurl.com/api-create.php?url={str}"
            response = requests.get(api_url)
            return response.text

        MyLink = pyperclip.paste()

        Fixed_Link = MyLink.replace("twitter.com", "vxtwitter.com").replace("x.com", "vxtwitter.com").replace("bsky.app", "r.bskyx.app").replace("instagram.com", "ddinstagram.com")

        if mode == "short":
            shortlink = tinyLink(Fixed_Link)
            pyperclip.copy(shortlink)
        elif mode == "long":
            pyperclip.copy(Fixed_Link)
        elif mode == "tiny":
            MyLink = tinyLink(MyLink)
            pyperclip.copy(MyLink)
        else:
            sys.exit(1)

        winsound.PlaySound(r'.\sound\done.wav', winsound.SND_FILENAME)
        sys.exit(1)

if __name__ == "__main__":
    LinkFix()