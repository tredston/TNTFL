from time import time
from urllib.request import urlopen

from tntfl.game import Game


class GameStore(object):

    def __init__(self, ladderFilePath):
        self._ladderFilePath = ladderFilePath

    def getGames(self):
        games = []
        ladder = urlopen(self._ladderFilePath)
        for line in ladder:
            gameLine = line.decode('utf-8').split()
                numParts = len(gameLine)
                # Red player, red score, blue player, blue score, time[, deletedBy, deletedAt]
                if numParts == 5 or numParts == 7:
                    game = Game(gameLine[0], gameLine[1], gameLine[2], gameLine[3], gameLine[4])
                    games.append(game)
                    if numParts == 7:
                        game.deletedBy = gameLine[5]
                        game.deletedAt = int(gameLine[6])
        return games

    def appendGame(self, game):
        with open(self._ladderFilePath, 'a') as ladder:
            self._writeGame(ladder, game)

    def deleteGame(self, gameTime, deletedBy, deletedAt=time()):
        games = self.getGames()
        found = False
        for game in games:
            if game.time == gameTime:
                game.deletedAt = deletedAt
                game.deletedBy = deletedBy
                found = True
                break
        if found:
            with open(self._ladderFilePath, 'w') as ladder:
                for game in games:
                    self._writeGame(ladder, game)
        return found

    def _writeGame(self, ladder, game):
        toWrite = "\n%s %s %s %s %.0f" % (game.redPlayer, game.redScore, game.bluePlayer, game.blueScore, game.time)
        if game.isDeleted():
            toWrite += " %s %.0f" % (game.deletedBy, game.deletedAt)
        ladder.write(toWrite)
