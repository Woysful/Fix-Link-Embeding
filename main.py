import sys, os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, 'lib'))
sys.path.append(os.path.join(parent_folder_path, 'plugin'))

from flowlauncher import FlowLauncher

class ContextMenu:
    def context_menu(self, data):
        return [
            {
                "Title"     : "Replacements list",
                "SubTitle"  : "Open config.JSON",
                "IcoPath"   : "Images\\config.png",
                "Score"     : 10000,
                "JsonRPCAction": {
                    "method"    : "open_replacements",
                    "parameters": [],
                    "dontHideAfterAction": False
                }
            }
        ]

    def open_replacements(self):
        os.startfile(r".\plugin\replacements.json")

class NoLink(FlowLauncher, ContextMenu):
    def query(self, query):
        return [
            {
                "Title"     : "Copy the link first!",
                "SubTitle"  : "it looks like you didn't copy the link",
                "IcoPath"   : "Images\\Warning.png"
            }
        ]
    
    def context_menu(self, data):
        return ContextMenu.context_menu(self, data)
    
class FixLink(FlowLauncher, ContextMenu):
    def query(self, query):
        return [
            {
                "Title": "Fixed Short Link",
                "SubTitle"  : config.domain_fix[0] + " | " + config.api_name,
                "IcoPath"   : "Images\\FixedTiny.png",
                "Score"     : 100000,
                "JsonRPCAction": {
                    "method"    : "run_fix",
                    "parameters": ["short"],
                    "dontHideAfterAction": False
                }
            },
            {
                "Title"     : "Fixed Link",
                "SubTitle"  : config.domain_fix[0],
                "IcoPath"   : "Images\\Fixed.png",
                "Score"     : 50000,
                "JsonRPCAction": {
                    "method"    : "run_fix",
                    "parameters": ["long"],
                    "dontHideAfterAction": False
                }
            },
            {
                "Title"     : "Short Link",
                "SubTitle"  : config.api_name,
                "IcoPath"   : "Images\\TinyLink.png",
                "Score"     : 0,
                "JsonRPCAction": {
                    "method"    : "run_fix",
                    "parameters": ["tiny"],
                    "dontHideAfterAction": False
                }
            }
        ]
    
    def context_menu(self, data):
        return ContextMenu.context_menu(self, data)

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