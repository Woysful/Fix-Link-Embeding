import sys, os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher
from plugin.utils import run, config

class link_fix(FlowLauncher):
    def query(self, query): 
        if not config.url_pattern.match(config.url):
            bad_link = [
                {
                    "Title": "Copy the link first!",
                    "SubTitle": "it looks like you didn't copy the link",
                    "IcoPath": "Images\\Warning.png",
                }
            ]
            return bad_link

        else:
            main = [
                {
                    "Title": "Fixed Tiny Link",
                    "SubTitle": config.domain_fix + " | " + config.api_name,
                    "IcoPath": "Images\\FixedTiny.png",
                    "Score": 100000,
                    "JsonRPCAction": {
                        "method": "run_fix",
                        "parameters": ["short"],
                        "dontHideAfterAction": False
                    }
                },
                {
                    "Title": "Fixed Link",
                    "SubTitle": config.domain_fix,
                    "IcoPath": "Images\\Fixed.png",
                    "Score": 50000,
                    "JsonRPCAction": {
                        "method": "run_fix",
                        "parameters": ["long"],
                        "dontHideAfterAction": False
                    }
                },
                {
                    "Title": "Shorten Link",
                    "SubTitle": config.api_name,
                    "IcoPath": "Images\\TinyLink.png",
                    "Score": 0,
                    "JsonRPCAction": {
                        "method": "run_fix",
                        "parameters": ["tiny"],
                        "dontHideAfterAction": False
                    }
                }
            ]
            return main

    def run_fix(self, arg):
        run(arg)

if __name__ == "__main__":
    link_fix()