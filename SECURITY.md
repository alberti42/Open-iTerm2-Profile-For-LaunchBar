# Security Policy

## Supported versions

Only the latest release receives fixes. To update, download `Open-iTerm2-Profile-For-LaunchBar.zip` from the [latest release](https://github.com/alberti42/Open-iTerm2-Profile-For-LaunchBar/releases/latest) and install the action again.

## Reporting a vulnerability

Report a vulnerability privately through GitHub: open the [Security tab](https://github.com/alberti42/Open-iTerm2-Profile-For-LaunchBar/security) of this repository and choose **Report a vulnerability**. Do not open a public issue for a vulnerability.

Include the version of the action (`CFBundleVersion` in the action's `Contents/Info.plist`), the macOS version, and the steps to reproduce the problem.

## What the action does that matters for security

- The action runs two Python scripts and one AppleScript in `Contents/Scripts/`, with the `python3` found in LaunchBar's `PATH`:

  | Script | What it does |
  |---|---|
  | `default.py` | Reads `~/Library/Preferences/com.googlecode.iterm2.plist`, which iTerm2 writes, and prints the `Name` of each profile under `New Bookmarks` as JSON to LaunchBar. |
  | `open_profile.py` | Runs `osascript iterm2_launcher.scpt` with the profile name you chose. |
  | `iterm2_launcher.scpt` | Tells iTerm2 to open a new tab with the profile in the current window, or a new window if none is open, and tells LaunchBar to hide. |

  The AppleScript sends Apple Events to iTerm2 and LaunchBar; macOS can ask you to allow LaunchBar to control iTerm2 (System Settings › Privacy & Security › Automation).
- The scripts write no file and make no network connection.
- The action in a release is built by GitHub Actions from the tagged source. The `.lbaction` bundle is signed with a Developer ID with the hardened runtime and notarized by Apple; the signature seals the three scripts. The bundle's executable, `Contents/MacOS/OpenITerm2Profile`, is a small program compiled from `Stub/main.c` that does nothing; LaunchBar does not run it. Gatekeeper fetches the notarization ticket online the first time you open the action. `Open-iTerm2-Profile-For-LaunchBar.zip` carries a build provenance attestation. To check where a downloaded `Open-iTerm2-Profile-For-LaunchBar.zip` was built:

  ```sh
  gh attestation verify Open-iTerm2-Profile-For-LaunchBar.zip --repo alberti42/Open-iTerm2-Profile-For-LaunchBar
  ```

  The attestation names the workflow (`.github/workflows/draft-release.yml`), the tag and the commit the ZIP was built from.
- To check a downloaded action before you install it:

  ```sh
  spctl --assess --type open --context context:primary-signature --verbose "Open iTerm2 Profile.lbaction"
  ```

  Gatekeeper answers `accepted` and `source=Notarized Developer ID`.
