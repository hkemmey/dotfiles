import os
import sys
import argparse

HOME = os.getenv("XDG_CONFIG_HOME", os.getenv("HOME"))

def create_link(source: str, to: str):
    if os.path.exists(to):
        os.rename(to, f"{to}.bak") #disable old configs without deleting

    os.symlink(os.path.abspath(source), to)

def remove_link(to: str):
    if os.path.islink(to):
        os.unlink(to)
        if os.path.exists(f"{to}.bak"):
            os.rename(f"{to}.bak", to)
    else:
        print(f"cannot unlink nonexistant link: {to}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--uninstall", action="store_true", required=False)
    
    args = parser.parse_args()
    
    if args.uninstall:
        ## remove links and rename .bak files
        remove_link(f"{HOME}/.wezterm.lua")
        remove_link(f"{HOME}/.config/zed/keymap.json")
        remove_link(f"{HOME}/.config/zed/settings.json")
    else:
        ## create links
        create_link("wezterm/.wezterm.lua", f"{HOME}/.wezterm.lua")
        create_link("zed/keymap.json", f"{HOME}/.config/zed/keymap.json")
        create_link("zed/settings.json", f"{HOME}/.config/zed/settings.json")

    ## exits
    sys.exit()
