# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- This change log.
- The `SteamWebClient.get_player_steam_level()` method.
- The `SteamWebClient.get_player_badges()` method.
- The `SteamWebClient.get_games_owned_by_user()` method.

### Fixed

- The `BaseClient.steam_id` attribute is now an `int`, which is what
  Steam returns itself from its API.

## [0.1.0] - 2024-01-07
