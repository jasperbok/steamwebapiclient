from .generated_client import BaseClient


class SteamWebClient(BaseClient):
    def get_player_steam_level(self, steam_id: int = None) -> int:
        """Return the level of a Steam user."""
        if not steam_id:
            steam_id = self.steam_id

        api_data = self.playerservice_getsteamlevel(self.key, steam_id)
        return api_data["response"]["player_level"]
