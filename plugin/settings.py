from os             import path
from json           import load
from urllib.parse   import urlparse

class Config:
    def __init__(self, url):
        # getting Flow Launcher user settings
        current_dir = path.dirname(path.abspath(__file__))
        root_dir    = path.abspath(path.join(current_dir, "..", "..", ".."))

        # settings path
        self.replacements_path  = r".\plugin\replacements.json"
        self.settings_path      = path.join(root_dir, "Settings", "Plugins", "Fix Link", "settings.json")
        
        self.settings_full      = self.load_json(self.settings_path)
        self.replace_full       = self.load_json(self.replacements_path)

        self.sound              = self.settings_full.get("sound", True)
        self.msg                = self.settings_full.get("win_msg", True)
        self.api_name           = self.settings_full.get("api_name", "TinyURL")

        self.domain, self.suffix = self.get_domain_and_suffix(url)
        self.domain_visual = self.domain_edit(self.domain, {
            "youtu"     : "YouTube",
            "youtube"   : "YouTube",
            "x"         : "Twitter",
            "twitter"   : "Twitter",
            "bsky"      : "Bluesky",
            "tumblr"    : "Tumblr",
            "instagram" : "Instagram",
            "twitch"    : "Twitch",
            "reddit"    : "Reddit",
            "bilibili"  : "BiliBili",
            "snapchat"  : "Snapchat",
            "threads"   : "Threads",
            "vimeo"     : "Vimeo",
            "tiktok"    : "Tiktok"
        })

        self.domain_fix = [self.replace_full.get(self.domain + "." + self.suffix, False), True]
        if not self.domain_fix[0]:
            self.domain_fix = ["No fix replacement", False]

    # load settings
    def load_json(self, path_):
        try:
            with open(path_, "r", encoding="utf-8") as f:
                return load(f)
        except:
            return {}
    
    # parse domain / suffix
    def get_domain_and_suffix(self, url):
        parsed_url = urlparse(url)
        hostname = parsed_url.hostname
        
        if not hostname:
            return None, None
        
        parts = hostname.split('.')
        
        if len(parts) < 2:
            return hostname, ''

        suffix = parts[-1]
        domain = parts[-2]

        return domain, suffix
    
    def domain_edit(self, domain, rep):
        return rep.get(domain, domain)