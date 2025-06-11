import sys, os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher

class NoLink(FlowLauncher):
    def query(self, query):
        return [
            {
                "Title": "Copy the link first!",
                "SubTitle": "it looks like you didn't copy the link",
                "IcoPath": "Images\\Warning.png",
            }
        ]
    
class FixLink(FlowLauncher):
    def query(self, query):
        return [
            {
                "Title": "Fixed Short Link",
                "SubTitle": config.domain_fix[0] + " | " + config.api_name,
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
                "SubTitle": config.domain_fix[0],
                "IcoPath": "Images\\Fixed.png",
                "Score": 50000,
                "JsonRPCAction": {
                    "method": "run_fix",
                    "parameters": ["long"],
                    "dontHideAfterAction": False
                }
            },
            {
                "Title": "Short Link",
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

    def run_fix(self, arg):
        from plugin.utils import run
        run(arg, config, url)

if __name__ == "__main__":
    from plugin.check import url_valid
    valid, url = url_valid()
    if not valid:
        NoLink()
    else:
        from plugin.settings import Config
        config = Config(url)
        FixLink()