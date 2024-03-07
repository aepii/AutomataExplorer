class FormalLanguage:
    def __init__(self, alphabet=None):
        if alphabet is None:
            self.alphabet = []
        else:
            self.alphabet = alphabet.split(",")

    # Add symbol to alphabet.
    def add(self, symbol):
        if symbol not in self.alphabet:
            self.alphabet.append(symbol)

    # Remove symbol from alphabet.
    def remove(self, symbol):
        if symbol in self.alphabet:
            self.alphabet.remove(symbol)

    # Determine if a string is in the language.
    def is_a_string(self, string):
        return all(character in self.alphabet for character in string)

    # Generate strings based on a given length.
    def generate_strings(self, length):

        # Initialize strings with lambda, an empty string.
        strings = ["λ"]

        # Generate strings recursively for every symbol in the alphabet.
        for i in range(len(self.alphabet)):
            strings.append(self._generate_string([], "", self.alphabet[i], length))

        strings = self._flatten_strings(strings) # Flatten the array of strings into one array.
        strings = self._sort_strings(strings) # Sort the array of strings.

        return strings

    # Helper method for generating strings.
    def _generate_string(self, strings, string, letter, length):
       
        # Base case.
        if len(string) == length:
            return

        string += letter # Add the letter to the string.
        strings.append(string) # Append the string to the array of strings.

        # Generate strings recursively for every symbol in the alphabet.
        for i in range(len(self.alphabet)):
            self._generate_string(strings, string, self.alphabet[i], length)

        return strings

    # Combine an array of strings into one array.
    @staticmethod
    def _flatten_strings(strings):
        new_strings = []
        for row in strings:
            new_strings.extend(row)

        return new_strings

    # Sort strings.
    def _sort_strings(self, strings):
        return sorted(strings, key=self._canonical_sort)
    
    # Standard sorting notation for languages.
    @staticmethod
    def _canonical_sort(s):
        # Sort by length and prioritize lambda.
        return (len(s) if s != "λ" else -1), s
