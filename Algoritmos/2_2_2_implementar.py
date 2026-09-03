from collections import deque

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

# ============================================================
# 1. Implemente la función que juega en base a un jugador dado (MAX o MIN)
# ============================================================

class TreeGame(Game):
    def __init__(self, initial_state, players, nodes):
        super().__init__(initial_state, players )
        self.nodes = nodes

    def is_terminal(self, state):
        return isinstance(state, (int, float))

    def depth(self, state):
        queue = deque()
        level = 0
        queue.append((self.initial_state, level))
        while queue:
            node, node_depth = queue.popleft()
            if node == state:
                return node_depth
            if state.is_terminal:
                continue
            level += 1
            for successor in node.values():
                queue.append(successor, level)

    def player(self, state):
        state =



def play_game(game, player):
    state = game.initial
    steps = [state]

    while not game.is_terminal(state):
        pass # IMPLEMENTE

    return steps




