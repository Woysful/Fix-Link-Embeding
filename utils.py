import pyperclip, requests, winsound, sys, os, json, re
from urllib.parse import quote_plus

class config():
    # getting Flow Launcher user settings
    def load_settings(settings_path = os.path.expandvars(r'%APPDATA%\FlowLauncher\Settings\Plugins\Fix Link\settings.json')):
        try:
            with open(settings_path, "r", encoding="utf-8") as f:
                settings = json.load(f)
            return settings
        except:
            return {}
    
    # getting replacements list from config.json
    def load_replacements(replacements_path = 'replacements.json'):
        try:
            with open(replacements_path, "r", encoding="utf-8") as f:
                replacements = json.load(f)
            return replacements
        except:
            return {}
    
    settings_full   = load_settings()
    replace_full    = load_replacements()

    # getting and validating URL from clipboard
    url             = pyperclip.paste().strip()
    url_pattern     = re.compile(
    r'((http[s]?://)?(www\.)?'
    r'([a-zA-Z0-9\-]+\.)+[a-zA-Z]{2,}'
    r'(/[^\s]*)?)')

    sound_notify    = settings_full.get("sound", True)
    api_name        = settings_full.get("api_name", "TinyURL")

# making url tiny
def tiny_url(url):
    try:
        match config.api_name:
            case "TinyURL":
                response = requests.get(f"https://tinyurl.com/api-create.php?url={quote_plus(url)}", timeout=5)
                if response.ok:
                    return response.text
            case "CleanURI":
                response = requests.post("https://cleanuri.com/api/v1/shorten", data={"url": url}, timeout=5)
                if response.ok:
                    return response.json().get("result_url")
            case "Spoo.me":
                response = requests.post("https://spoo.me", data={"url" : url}, headers={"Accept": "application/json"}, timeout=5)
                if response.ok:
                    return response.json().get("short_url")
    except:
        winsound.PlaySound(r'.\sound\warning.wav', winsound.SND_FILENAME)
        sys.exit(1)

def run(arg):
    # fixing url based on replacements.json
    url_fixed = config.url
    for old, new in config.replace_full.items():
        if old in config.url:
            url_fixed = config.url.replace(old, new)
            break

    # action based on button user clicked
    match arg:
        case "short":
            url_short = tiny_url(url_fixed)
            pyperclip.copy(url_short)
        case "long":
            pyperclip.copy(url_fixed)
        case "tiny":
            config.url = tiny_url(config.url)
            pyperclip.copy(config.url)
        case _:
            sys.exit(1)
    
    if config.sound_notify == "true":
        winsound.PlaySound(r'.\sound\done.wav', winsound.SND_FILENAME)
    sys.exit(1)
