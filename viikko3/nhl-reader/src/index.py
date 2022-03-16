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
            name = f"{player_dict['name']:20}"
            team = f"{player_dict['team']:5}"
            goals = player_dict['goals']
            assists = player_dict['assists']
            sum = goals + assists
            total = str(sum)
            player = Player(
                 name + team + f"{str(goals):2}" + " + " + f"{str(assists):2}" + " = " + total
            )
            players.append(player)


    print("Players from FIN:")

    for player in players:
        print(player)


if __name__ == "__main__":
    main()

