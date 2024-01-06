class SteamWebClient:
    api_key: str
    profile_id: str
    default_lang: str

    def __init__(self, api_key, profile_id="", default_lang="en"):
        self.api_key = api_key
        self.profile_id = profile_id
        self.default_lang = default_lang
