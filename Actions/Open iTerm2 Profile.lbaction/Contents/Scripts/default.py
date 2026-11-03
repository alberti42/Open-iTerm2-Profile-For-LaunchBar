#!/usr/bin/env -S -P/usr/local/bin:${PATH} python3
# coding: utf-8
#
# LaunchBar Action Script

import json
import plistlib
from pathlib import Path

# Path to iTerm2 preferences file
ITERM_PLIST_PATH = Path.home() / "Library/Preferences/com.googlecode.iterm2.plist"

def get_iterm_profiles():
    """Reads iTerm2 profiles from preferences plist file; None if the file is missing."""
    if not ITERM_PLIST_PATH.exists():
        return None
    
    with ITERM_PLIST_PATH.open("rb") as f:
        plist_data = plistlib.load(f)

    # Extract profiles from "New Bookmarks" key
    profiles = plist_data.get("New Bookmarks", [])
    return [profile["Name"] for profile in profiles if "Name" in profile]

def main():
    """Returns iTerm2 profiles in LaunchBar format."""
    profiles = get_iterm_profiles()

    if profiles is None:
        items = [{"title": "iTerm2 preferences not found", "icon": "com.googlecode.iterm2"}]
    elif not profiles:
        items = [{"title": "No iTerm2 profiles found", "icon": "com.googlecode.iterm2"}]
    else:
        items = [
            {
                "title": profile,
                "subtitle": "Create new tab with this profile",
                "icon": "com.googlecode.iterm2",
                "action": "open_profile.py",
                "actionArgument": profile,
                "actionReturnsItems": False
            }
            for profile in profiles
        ]

    print(json.dumps(items))

if __name__ == "__main__":
    main()
