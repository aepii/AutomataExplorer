class State:
    def __init__(self, name, accepting):
        self.name = name
        self.accepting = accepting
        self.transitions = {}

    def add(self, letter, state):
        self.transitions[letter] = state

    def count_edges(self):
        return len(self.transitions)


class Automata:
    def __init__(self, states, initial_state):
        self.states = states
        self.current_state = initial_state

    def process_input(self, input_string):
        for symbol in input_string:
            if symbol in self.current_state.transitions:
                past_state = self.current_state.name
                self.current_state = self.current_state.transitions[symbol]
                print(f"{past_state}: {symbol} --> {self.current_state.name}")
            else:
                print(f"No path found for {symbol} in state {self.current_state.name}.")
                return

        if self.current_state.accepting:
            print(f"{input_string} is accepted.")
        else:
            print(f"{input_string} is not accepted.")