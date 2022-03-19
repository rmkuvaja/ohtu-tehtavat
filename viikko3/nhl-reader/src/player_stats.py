from player import Player
from player_reader import PlayerReader

class PlayerStats:
    def __init__(self, PlayerReader):
        reader = PlayerReader
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        players = []
        for line in self._players:
            if line['nationality'] == nationality:
                name = f"{line['name']:20}"
                team = f"{line['team']:5}"
                goals = line['goals']
                assists = line['assists'] 
                points = goals + assists
                player = Player(
                    name, team, goals, assists, points
                )
                players.append(player)
            sorted_players=sorted(players, reverse=True, key=lambda player: player.points) 
        return sorted_players
