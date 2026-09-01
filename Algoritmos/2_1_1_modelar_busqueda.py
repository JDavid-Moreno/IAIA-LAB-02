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