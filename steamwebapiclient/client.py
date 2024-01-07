from typing import List

from .generated_client import BaseClient
from .objects import Badge


class SteamWebClient(BaseClient):
    def get_player_steam_level(self, steam_id: int = None) -> int:
        """Return the level of a Steam user."""
        if not steam_id:
            steam_id = self.steam_id

        api_data = self.playerservice_getsteamlevel(self.key, steam_id)
        return api_data["response"]["player_level"]

    def get_player_badges(self, steam_id: int = None) -> List[Badge]:
        """Return a Steam user's badges."""
        if not steam_id:
            steam_id = self.steam_id

        api_data = self.playerservice_getbadges(self.key, steam_id)

        return [
            Badge.from_api_response(x) for x in api_data["response"].get("badges", [])
        ]
