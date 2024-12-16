import json

from utils import lookupFunctions
from utils import constants

team_details = {
    "Packers": {
        "team_id": constants.PACKERS_TEAM_ID,
        "league_id": constants.NFL_LEAGUE_ID,
        "yearly_results": {},
    },
    "Wild": {
        "team_id": constants.WILD_TEAM_ID,
        "league_id": constants.NHL_LEAGUE_ID,
        "yearly_results": {},
    },
    "Bucks": {
        "team_id": constants.BUCKS_TEAM_ID,
        "league_id": constants.NBA_LEAGUE_ID,
        "yearly_results": {},
    },
    "Liverpool": {
        "team_id": constants.LIVERPOOL_TEAM_ID,
        "league_id": constants.EPL_LEAGUE_ID,
        "yearly_results": {},
    }
}

for team in team_details:
    for year in range(constants.INITIAL_LOOKUP_YEAR, constants.FINAL_LOOKUP_YEAR + 1):
        year_string = str(year)
        if team_details[team]["league_id"] != constants.NFL_LEAGUE_ID:
            year_string = f"{year}-{year + 1}"
        team_events = lookupFunctions.lookup_season_events(team_details[team]["league_id"], year_string, team)
        team_details[team]["yearly_results"][year_string] = team_events

print(json.dumps(team_details, indent=4))