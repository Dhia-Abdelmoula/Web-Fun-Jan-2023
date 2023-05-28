# kevin = {
#     "name": "Kevin Durant",
#     "age": 34,
#     "position": "small forward",
#     "team": "Brooklyn Nets",
# }
# jason = {
#     "name": "Jason Tatum",
#     "age": 24,
#     "position": "small forward",
#     "team": "Boston Celtics",
# }
# kyrie = {
#     "name": "Kyrie Irving",
#     "age": 32,
#     "position": "Point Guard",
#     "team": "Brooklyn Nets",
# }

players = [
    {
        "name": "Kevin Durant",
        "age": 34,
        "position": "small forward",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Jason Tatum",
        "age": 24,
        "position": "small forward",
        "team": "Boston Celtics",
    },
    {
        "name": "Kyrie Irving",
        "age": 32,
        "position": "Point Guard",
        "team": "Brooklyn Nets",
    },
    {
        "name": "Damian Lillard",
        "age": 33,
        "position": "Point Guard",
        "team": "Portland Trailblazers",
    },
    {
        "name": "Joel Embiid",
        "age": 32,
        "position": "Power Foward",
        "team": "Philidelphia 76ers",
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls",
    },
]


# Create your Player instances here!
# player_jason = ???


class Player:
    def __init__(self, players_info):
        self.name = players_info["name"]
        self.age = players_info["age"]
        self.position = players_info["position"]
        self.team = players_info["team"]


# player_kyrie = Player(kyrie)
# player_jason = Player(jason)
# player_kevin = Player(kevin)


new_team = []
for player_info in players:
    player = Player(player_info)
    new_team.append(player)


