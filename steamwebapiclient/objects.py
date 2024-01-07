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
