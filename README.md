# Open iTerm2 Profile for LaunchBar

[![made for LaunchBar](https://img.shields.io/badge/made%20for-LaunchBar-blue)](https://www.obdev.at/products/launchbar/index.html)
[![notarized download](https://img.shields.io/github/actions/workflow/status/alberti42/Open-iTerm2-Profile-For-LaunchBar/verify-release.yml?label=notarized%20download&logo=apple)](https://github.com/alberti42/Open-iTerm2-Profile-For-LaunchBar/actions/workflows/verify-release.yml)
[![license](https://img.shields.io/github/license/alberti42/Open-iTerm2-Profile-For-LaunchBar)](LICENSE)

This repository provides an action for [LaunchBar](https://www.obdev.at/products/launchbar/actions.html) that allows users to quickly open a terminal session using any available [iTerm2](https://iterm2.com/) profile. The action lists all configured profiles in iTerm2, and selecting one from the dropdown menu in LaunchBar opens a new tab with the chosen profile in an existing iTerm2 window. If no iTerm2 window is open, a new window is launched.

![Screenshot](Images/iTerm2_profiles_list_screenshot.jpg)

## Contents

This repository includes the following components:

- **Open iTerm2 Profile.lbaction**: the LaunchBar action. The action is in `Actions/`; `Open-iTerm2-Profile-For-LaunchBar.zip`, attached to each [release](https://github.com/alberti42/Open-iTerm2-Profile-For-LaunchBar/releases), contains it. Its scripts, in `Contents/Scripts/`:
  - `default.py` – Retrieves available iTerm2 profiles and provides them to LaunchBar.
  - `iterm2_launcher.scpt` – AppleScript for opening a new tab or window with the selected profile.
  - `open_profile.py` – Handles profile selection and executes the appropriate script to launch iTerm2.

## Installation

### Option 1: Manual Installation

1. **Download** [Open-iTerm2-Profile-For-LaunchBar.zip](https://github.com/alberti42/Open-iTerm2-Profile-For-LaunchBar/releases/latest/download/Open-iTerm2-Profile-For-LaunchBar.zip) from the latest release.
2. **Extract** the zip to get `Open iTerm2 Profile.lbaction`.
3. Move `Open iTerm2 Profile.lbaction` to the LaunchBar Actions folder:
   ```
   ~/Library/Application Support/LaunchBar/Actions
   ```
4. **Restart LaunchBar** to load the new action.

### Option 2: Automatic Installation

Simply double-click the `Open iTerm2 Profile.lbaction` file. This will install the action automatically in LaunchBar.

## Compilation Instructions

Compilation from the source code is not necessary if you simply plan to use the action. The action in the released `Open-iTerm2-Profile-For-LaunchBar.zip` is signed with a Developer ID and notarized by Apple. Requirements: Xcode or the Xcode Command Line Tools.

1. **Build** the action:
   ```
   bin/build_actions.sh
   ```
   The script copies the files of `Actions/Open iTerm2 Profile.lbaction` that git tracks to `build/Actions/`, compiles `Stub/main.c` for arm64 and x86_64 into the bundle's `Contents/MacOS/OpenITerm2Profile`, signs the bundle, and packs it into `build/Open-iTerm2-Profile-For-LaunchBar.zip`. Without an argument it signs ad hoc. To sign with a Developer ID, give the identity as argument:
   ```
   bin/build_actions.sh "Developer ID Application: Your Name (TEAMID)"
   ```
   LaunchBar runs the scripts in `Contents/Scripts/`, not the compiled program. The program is the bundle's executable so that the bundle's signature, which seals the scripts, can be notarized: Apple's notary service issues tickets only for compiled code.

2. **Install** the built action by double-clicking `build/Actions/Open iTerm2 Profile.lbaction`, or copy it to:
   ```
   ~/Library/Application Support/LaunchBar/Actions
   ```

## Releasing

`CHANGELOG.md` is based on [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html). Pre-releases carry a `-beta.N` suffix (`vX.Y.Z-beta.N`).

1. Describe the changes under `## [Unreleased]` in `CHANGELOG.md` (Keep a Changelog 1.1.0).
2. `bin/bump_version.sh vX.Y.Z` (or `vX.Y.Z-beta.N`): sets `CFBundleVersion` in `Actions/*.lbaction/Contents/Info.plist`, moves the `[Unreleased]` entries under the version with `bin/changelog.py` (releases only), commits and tags.
3. `git push origin main --tags`. The tag starts `.github/workflows/draft-release.yml`: build with the Developer ID, notarize `Open-iTerm2-Profile-For-LaunchBar.zip` with `notarytool`, attest its build provenance, and create a draft release with `Open-iTerm2-Profile-For-LaunchBar.zip`. The release notes are the version's `CHANGELOG.md` section and a link to the commits since the previous tag. The workflow fails if the tag does not match `CFBundleVersion`.
4. Publish the draft on GitHub. `.github/workflows/verify-release.yml` then checks the published `Open-iTerm2-Profile-For-LaunchBar.zip` (provenance, signature, team, notarization); it also runs weekly.

To verify a downloaded `Open-iTerm2-Profile-For-LaunchBar.zip`:
```
gh attestation verify Open-iTerm2-Profile-For-LaunchBar.zip --repo alberti42/Open-iTerm2-Profile-For-LaunchBar
```

## Usage

- Open **LaunchBar** and type `iTerm2` or part of the action name.
- Select **"Open iTerm2 Profile"**.
- A dropdown menu will appear, listing all available iTerm2 profiles.
- Choose a profile to open a new tab in the existing iTerm2 window, or a new window if none is open.

## Requirements

- macOS
- [LaunchBar](https://www.obdev.at/products/launchbar/)
- [iTerm2](https://iterm2.com/)

## Security

To report a vulnerability, see [SECURITY.md](SECURITY.md).

## Donations

If you find this action useful, consider supporting its development with a donation.

[<img src="Images/buy_me_coffee.png" width=300 alt="Buy Me a Coffee QR Code"/>](https://buymeacoffee.com/alberti)

## Author

- **Author:** Andrea Alberti
- **GitHub Profile:** [alberti42](https://github.com/alberti42)
- **Donations:** [![Buy Me a Coffee](https://img.shields.io/badge/Donate-Buy%20Me%20a%20Coffee-orange)](https://buymeacoffee.com/alberti)

Feel free to contribute to the development of this action or report any issues in the [GitHub repository](https://github.com/alberti42/Open-iTerm2-Profile-For-LaunchBar/issues).
