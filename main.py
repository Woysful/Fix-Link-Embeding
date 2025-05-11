import sys,os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
from utils import run

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

    def run_fix(self, arg):
        run(arg)

if __name__ == "__main__":
    LinkFix()