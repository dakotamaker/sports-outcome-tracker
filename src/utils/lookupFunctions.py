import requests
import pathlib
import json

from . import constants

curPath = pathlib.Path(__file__).parent.parent.parent.resolve()

with open(f"{curPath}/envVars.json") as f:
    data = json.load(f)

API_KEY = data["API_KEY"]

def lookup_season_events(league_id, season_string, team_name):
    api_call = requests.get(f"{constants.API_BASE_URL}/api/v1/json/{API_KEY}/eventsseason.php?id={league_id}&s={season_string}")
    storage = api_call.json()
    events = [event for event in storage["events"] if (event["strHomeTeam"] == team_name or event["strAwayTeam"] == team_name) and event["intRound"] != constants.PRE_SEASON_ROUND_ID]
    cleaned_events = []
    for event in events:
        team_loc = "Away" if event["strAwayTeam"] == team_name else "Home"
        opponent_loc = "Away" if event["strHomeTeam"] == team_name else "Home"

        cleaned_event = {
            "date": event["dateEvent"],
            "loc": team_loc,
            "opponent": event[f"str{opponent_loc}Team"],
            "result": "Tie" if event["intHomeScore"] == event["intAwayScore"] else "Win" if event[f"int{team_loc}Score"] > event[f"int{opponent_loc}Score"] else "Loss"
        }

        cleaned_events.append(cleaned_event)

    return cleaned_events