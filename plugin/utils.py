import requests
from sys            import exit
from pyperclip      import copy
from winsound       import PlaySound, SND_FILENAME
from urllib.parse   import quote_plus
from settings       import Config
from check          import url_valid

# sound notification
def sound_msg(status, config: Config):
    if config.sound:
        sound_file = r'.\sound\done.wav' if status else r'.\sound\warning.wav'
        PlaySound(sound_file, SND_FILENAME)    

def win_msg(status, type, config: Config):
    if config.msg:
        match type:
            case "shortfix":
                sub = "Short fixed link in clipboard!" if status else "Something goes wrong ¯\_(ツ)_/¯"
                ico = r"Images\FixedTiny.png" if status else r"Images\Warning.png"
            case "long":
                sub = "Fixed link in clipboard!" if status else "Something goes wrong ¯\_(ツ)_/¯"
                ico = r"Images\Fixed.png" if status else r"Images\Warning.png"
            case "tiny":
                sub = "Short link in clipboard!" if status else "Something goes wrong ¯\_(ツ)_/¯"
                ico = r"Images\TinyLink.png" if status else r"Images\Warning.png"
            case _:
                sub = "Something goes wrong ¯\_(ツ)_/¯"
                ico = r"Images\icon.png"

        from flowlauncher import FlowLauncherAPI
        FlowLauncherAPI.show_msg(
            title="Fix Link",
            sub_title=sub,
            # ico_path=ico - doesn't count custom icon for some reason ¯\_(ツ)_/¯
        )

# making url tiny
def tiny_url(url, config: Config):
    try:
        match config.api_name:
            case "TinyURL"  :
                response = requests.get(f"https://tinyurl.com/api-create.php?url={quote_plus(url)}", timeout=5)
                if response.ok:
                    return response.text
            case "CleanURI" :
                response = requests.post("https://cleanuri.com/api/v1/shorten", data={"url": url}, timeout=5)
                if response.ok:
                    return response.json().get("result_url")
            case "Spoo.me"  :
                response = requests.post("https://spoo.me", data={"url" : url}, headers={"Accept": "application/json"}, timeout=5)
                if response.ok:
                    return response.json().get("short_url")
    except:
        sound_msg(False, config)
        win_msg(False, False, config)
        exit(1)

def run(arg, config: Config, url):
    if not url_valid()[0]:
        sound_msg(False, config)
        win_msg(False, False, config)
        exit(1)
    else:
        # fixing url based on replacements.json
        url_fixed = url
        for old, new in config.replace_full.items():
            if old in url:
                url_fixed = url.replace(old, new)
                break

        # action based on button user clicked
        match arg:
            case "shortfix":
                if config.domain_fix[1]:
                    url_short = tiny_url(url_fixed, config)
                    copy(url_short)
            case "long":
                if config.domain_fix[1]:
                    copy(url_fixed)
            case "tiny":
                url = tiny_url(url, config)
                copy(url)
            case _:
                exit(1)
        
        sound_msg(True, config)
        win_msg(True, arg, config)
        exit(1)