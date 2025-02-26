import os
import sys

HOME = os.getenv("XDG_CONFIG_HOME", os.getenv("HOME"))

def create_link(source: str, to: str):
    os.symlink(os.path.abspath(source), f"{HOME}/{to}")

def remove_link(to: str):
    if os.path.islink(f"{HOME}/{to}"):
        os.unlink(f"{HOME}/{to}")
    else:
        print(f"cannot unlink nonexistant link: {HOME}/{to}")

if __name__ == '__main__':
    print(HOME)
    
    links: dict = {
        "wezterm/.wezterm.lua": ".wezterm.lua",
        "zed/keymap.json": ".config/zed/keymap.json",
        "zed/settings.json": ".config/zed/settings.json"
    }

    for key in links:
        print(f"{HOME}/{key}")
    sys.exit()
