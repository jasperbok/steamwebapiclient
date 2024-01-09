from dataclasses import dataclass
from typing import Optional


@dataclass
class Badge:
    id: int
    completion_time: int
    level: int
    scarcity: int
    xp: int
    app_id: Optional[int] = None
    border_color: Optional[int] = None
    community_item_id: Optional[str] = None

    @classmethod
    def from_api_response(cls, api_response: dict):
        return cls(
            api_response["badgeid"],
            api_response["completion_time"],
            api_response["level"],
            api_response["scarcity"],
            api_response["xp"],
            api_response.get("appid", None),
            api_response.get("border_color", None),
            api_response.get("communityitemid", None),
        )


@dataclass
class Game:
    id: int
    name: str
    img_icon_url: str
    playtime_forever: int
    playtime_windows_forever: int
    playtime_mac_forever: int
    playtime_linux_forever: int
    playtime_disconnected: int
    rtime_last_played: int
    has_community_visible_stats: bool
    has_leaderboards: bool

    @classmethod
    def from_api_response(cls, api_response: dict):
        return cls(
            api_response["appid"],
            api_response["name"],
            api_response["img_icon_url"],
            api_response["playtime_forever"],
            api_response["playtime_windows_forever"],
            api_response["playtime_mac_forever"],
            api_response["playtime_linux_forever"],
            api_response["playtime_disconnected"],
            api_response["rtime_last_played"],
            api_response.get("has_community_visible_stats", False),
            api_response.get("has_leaderboards", False),
        )
