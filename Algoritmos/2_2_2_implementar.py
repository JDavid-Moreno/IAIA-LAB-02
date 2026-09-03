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

#----------------------------------------

# ============================================================
# 2. Represente el espacio de búsqueda de ejemplo
# use como referencia el modelado del punto A
# ============================================================
class TreeGame(Game):
    def __init__(self, initial_state, players, nodes):
        super().__init__(initial_state, players )
        self.nodes = nodes

    def is_terminal(self, state):
        return isinstance(state, (int, float))

    def depth(self, state):
        queue = deque()
        queue.append((self.initial_state, 0))
        while queue:
            node, node_depth = queue.popleft()
            if node == state:
                return node_depth
            if self.is_terminal(node):
                continue
            for successor in self.nodes[node]:
                queue.append((successor, node_depth + 1))
        return -1

    def player(self, state):
        if self.depth(state) % 2 == 0:
            return self.players[0]
        else:
            return self.players[1]

    def opponent(self, player):
        if player == self.players[0]:
            return self.players[1]
        else:
            return self.players[0]

    def result_actions(self, state):
        if self.is_terminal(state):
            return set()
        else:
            return set(self.nodes[state])

    def utility(self, state, player):
        return float(state)

# ============================================================
# 1. Implemente la función que juega en base a un jugador dado (MAX o MIN)
# ============================================================

def play_game(game, player):
    state = game.initial_state
    steps = [state]

    while not game.is_terminal(state):
        shift = game.player(state)
        best_successor = None
        best_value = float('-inf') if shift == game.players[0] else float('inf')
        for successor in game.result_actions(state):
            value = MaxMinSearch.minmax_search(game, successor)
            if (shift == game.players[0]  and value > best_value) or (shift == game.players[1]  and value < best_value):
                best_value = value
                best_successor = successor

        state = best_successor
        steps.append(state)

    return steps

# ============================================================
# 3. Use la implementación del algoritmo de búsqueda min-max
# aplicándola al estado inicial del espacio de búsqueda ejemplo
# ============================================================

nodes = {
    "A": ["B", "C", "D"],
    "B": ["E", "F", "G"],
    "C": ["H", "I", "J"],
    "D": ["K", "L", "M"],
    "E": [8, 7, 2],
    "F": [9, 1, 6],
    "G": [2, 4, 1],
    "H": [1, 3, 5],
    "I": [3, 9, 2],
    "J": [6, 5, 2],
    "K": [1, 2, 3],
    "L": [9, 7, 2],
    "M": [16, 6, 4],
}

# ============================================================
# 4. Use la función `play_game` para jugar como MAX
# mostrando la secuencia de acciones y la utilidad final
# ============================================================

game = TreeGame(
    initial_state = "A",
    players = ("J1", "J2"),
    nodes = nodes
)

print("Secuencia de play_game:", play_game(game, "J1"))

