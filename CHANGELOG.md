# Changelog

All notable changes to the Open iTerm2 Profile action are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2026-11-03

### Fixed

- When `~/Library/Preferences/com.googlecode.iterm2.plist` was missing, the action showed a broken item instead of "iTerm2 preferences not found".

### Changed

- The action is signed with a Developer ID and notarized by Apple. The bundle contains a small executable, `Contents/MacOS/OpenITerm2Profile`, that LaunchBar does not run; it carries the signature, which seals the scripts.
- The action's bundle identifier is `Alberti42.LaunchBar.action.OpenITerm2Profile`, as in the author's other LaunchBar actions; it was `Alberti42.LaunchBar.action.iTerm2`. LaunchBar may treat the action as a new one: remove `Open iTerm2 Profile.lbaction` version 1.0 from `~/Library/Application Support/LaunchBar/Actions` before installing this version.
- `Open-iTerm2-Profile-For-LaunchBar.zip` is attached to each GitHub release, with a build provenance attestation. It replaces `Action Open iTerm2 Profile.lbaction.zip`, which was kept in the repository.

[Unreleased]: https://github.com/alberti42/Open-iTerm2-Profile-For-LaunchBar/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/alberti42/Open-iTerm2-Profile-For-LaunchBar/releases/tag/v2.0.0
