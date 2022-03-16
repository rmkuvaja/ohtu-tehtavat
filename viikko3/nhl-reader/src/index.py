import requests
from player import Player

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

#    print("JSON-muotoinen vastaus:")
#    print(response)

    players = []
    nationality = 'FIN'

    for player_dict in response:
        if player_dict['nationality'] == nationality:
            name = player_dict['name']
            team = player_dict['team']
            goals = player_dict['goals']
            assists = player_dict['assists']
            player = Player(
                 name + "team " + team + "  goals " + str(goals)  + "  assists " + str(assists)
            )
            players.append(player)


    print("Players from FIN:")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()

