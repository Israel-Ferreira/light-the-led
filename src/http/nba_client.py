from nba_api.stats.static.teams import find_teams_by_nickname
from nba_api.stats.endpoints import leaguegamefinder

import json


def get_team_last_game(team_name: str):
    
    team = find_teams_by_nickname("kings")[0]
    team_id = team['id']

    game_finder = leaguegamefinder.LeagueGameFinder(team_id_nullable=team_id)

    gf_dataframe = json.loads(game_finder.get_normalized_json())

    return gf_dataframe["LeagueGameFinderResults"][0]

