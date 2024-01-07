# Steam Web API Client

A Python client for the [Steam Web API](https://developer.valvesoftware.com/wiki/Steam_Web_API).

Valve provides [an API endpoint](http://api.steampowered.com/ISteamWebAPIUtil/GetSupportedAPIList/v0001/)
that describes all other endpoints. This is used to automatically
generate most of the code for this package.

## Installation

This package can be installed with pip:

```shell
pip install steamwebapiclient
```

## Usage

```python
from steamwebapiclient import SteamWebClient

client = SteamWebClient(
    key="YourApiKey",  # Only required if calling non-public API endpoints.
    steam_id="SomeSteamId",  # Scopes API calls that use this to this ID.
)

domains = client.steamdirectory_getsteampipedomains()
```

## Generating the Base Client Class

To regenerate the base client class from Valve's API definitions, run
the following from the root of the project (where this README is
located).

```shell
python generate_client.py [API_KEY]
```

The `API_KEY` argument is optional, but without it, only publicly
accessible methods will be available in the generated client code.

After regenerating the client, its code must be formatted using
[black](https://black.readthedocs.io/en/stable/index.html).

## License
