class Game:
    def __init__(self, initial_state, players):
        self.initial_state = initial_state
        self.players = players

    def player(self, state):
        pass

    def opponent(self, player):
        pass

    def is_terminal(self, state):
        return False

    def result_actions(self, state):
        return set()

    def utility(self, state, player):
        return 0.0

class MaxMinSearch:

    @staticmethod
    def max_value(game, state):
        if game.is_terminal(state):
            return game.utility(state, game.player(state))
        best_value = float('-inf')
        for successor in game.result_actions(state):
            value = MaxMinSearch.min_value(game, successor)
            best_value = max(best_value, value)
        return best_value

    @staticmethod
    def min_value(game, state):
        if game.is_terminal(state):
            return game.utility(state, game.player(state))
        worst_value = float ('inf')
        for successor in game.result_actions(state):
            value = MaxMinSearch.max_value(game, successor)
            worst_value = min(worst_value, value)
        return worst_value

    @staticmethod
    def minmax_search(game, state):
        if game.player(state) == game.players[0]:
            return MaxMinSearch.max_value(game, state)
        else:
            return MaxMinSearch.min_value(game, state)




