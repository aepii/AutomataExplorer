class FormalLanguage:
    def __init__(self):
        self.alphabet = []

    def add(self, symbol):
        if symbol not in self.alphabet:
            self.alphabet.append(symbol)

    def remove(self, symbol):
        if symbol in self.alphabet:
            self.alphabet.remove(symbol)

    def is_a_string(self, string):
        return all(character in self.alphabet for character in string)

    def generate_strings(self, length):
        strings = ["λ"]

        for i in range(len(self.alphabet)):
            strings.append(self._generate_string([], "", self.alphabet[i], length))

        strings = self._flatten_strings(strings)
        strings = self._sort_strings(strings)

        return strings

    def _generate_string(self, strings, string, letter, length):
        if len(string) == length:
            return

        string += letter
        strings.append(string)

        for i in range(len(self.alphabet)):
            self._generate_string(strings, string, self.alphabet[i], length)

        return strings

    @staticmethod
    def _flatten_strings(strings):
        new_strings = []
        for row in strings:
            new_strings.extend(row)

        return new_strings

    def _sort_strings(self, strings):
        return sorted(strings, key=self._canonical_sort)

    @staticmethod
    def _canonical_sort(s):
        return (len(s) if s != "λ" else -1), s
