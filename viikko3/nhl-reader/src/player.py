class Player:
    def __init__(self, name, team, goals, assists, points):
        self.name = name
        self.team = team
        self.goals = goals
        self.assists = assists
        self.points = points

    def __str__(self):
        return f"{self.name} {self.team} {self.goals} + {self.assists} = {self.points}"
