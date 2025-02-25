import os
import sys

HOME = os.getenv("XDG_CONFIG_HOME", os.getenv("HOME"))

def create_link(source: str, to: str):
    os.symlink(os.path.abspath(source), HOME.join(f"/{to}"))

def remove_link(to: str):
    if os.path.islink(HOME.join(f"{to}")):
        os.unlink(HOME.join(f"{to}"))
    else:
        print(f"cannot unlink nonexistant link: {HOME.join(f"{to}")}")

if __name__ == '__main__':
    print(HOME)
    
    links: dict = {
        "wezterm/.wezterm.lua": ".wezterm.lua",
        "zed/keymap.json": ".config/zed/keymap.json",
        "zed/settings.json": ".config/zed/settings.json"
    }

    sys.exit()
