#!/usr/bin/env -S -P/usr/local/bin:${PATH} python3
# coding: utf-8
#
# LaunchBar Action Script

import sys
import subprocess
from pathlib import Path

APPLESCRIPT_PATH = Path(__file__).parent / "iterm2_launcher.scpt"

def open_profile(profile_name):
    """Calls AppleScript to open iTerm2 with the given profile and close LaunchBar."""
    result = subprocess.run(["osascript", APPLESCRIPT_PATH, profile_name], capture_output=True, text=True)

    if result.stderr:
        # Add code to handle errors if they occur
        pass

if len(sys.argv) == 2:
    profile_name = sys.argv[1]
    open_profile(profile_name)
