class Player(object):
    def __init__(self):
        self.elo = 0.0


def getBlueGoalRatio(red, blue):
    return 1 / (1 + 10 ** ((red - blue) / 180))


def calculateSkillChange(red, blue, redScore, blueScore):
    predict = getBlueGoalRatio(red.elo, blue.elo)
    goals = blueScore + redScore
    result = blueScore / goals
    delta = (2.5 * goals) * (result - predict)
    return delta


def getPlayer(players, name):
    if name not in players:
        players[name] = Player()
    return players[name]


def do(games):
    players = {}
    for game in [g for g in games if not g.isDeleted()]:
        red = getPlayer(players, game.redPlayer)
        blue = getPlayer(players, game.bluePlayer)

        skillChangeToBlue = calculateSkillChange(red, blue, game.redScore, game.blueScore)
        red.elo -= skillChangeToBlue
        blue.elo += skillChangeToBlue
        game.skillChangeToBlue = skillChangeToBlue
    return games
