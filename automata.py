class Language:
    def __init__(self):
        self.alphabet = []

    def add(self, symbol):
        if symbol not in self.alphabet:
            self.alphabet.append(symbol)

    @staticmethod
    def _canonical_sort(s):
        return (len(s) if s != "λ" else -1), s

    def _sort_strings(self, strings):
        return sorted(strings, key=self._canonical_sort)

    def _generate_string(self, string, letter, length, strings):

        if len(string) == length:
            return

        string += letter
        strings.append(string)

        for i in range(len(self.alphabet)):
            self._generate_string(string, self.alphabet[i], length, strings)

        return strings

    @staticmethod
    def _flatten_strings(strings):

        new_strings = []
        for row in strings:
            new_strings.extend(row)

        return new_strings

    def generate_strings(self, length):

        strings = ["λ"]
        for i in range(len(self.alphabet)):
            strings.append(self._generate_string("", self.alphabet[i], length, []))

        strings = self._flatten_strings(strings)
        strings = self._sort_strings(strings)

        return strings


class State:
    def __init__(self, name):
        self.name = name
        self.transitions = set()
