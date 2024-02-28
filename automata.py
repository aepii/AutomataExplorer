class Language:
    def __init__(self):
        self.alphabet = []
        self.size = 0

    def add(self, symbol):
        if symbol not in self.alphabet:
            self.alphabet.append(symbol)
            self.size += 1

    def _generate_string(self, string, letter, length, strings):

        if len(string) == length:
            return

        string += letter
        strings.append(string)

        for i in range(len(self.alphabet)):
            self._generate_string(string, self.alphabet[i], length, strings)

        return strings

    def _flatten_list(self, list):

        new_list = []
        for row in list:
            new_list.extend(row)

        return new_list

    def generate_strings(self, length):

        strings = []
        for i in range(len(self.alphabet)):
            strings.append(self._generate_string("", self.alphabet[i], length, []))

        strings = self._flatten_list(strings)

        return strings


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = set()
