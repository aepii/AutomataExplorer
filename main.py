from automata import *


def main():
    my_language = Language()
    my_language.add("c")
    my_language.add("b")
    my_language.add("a")

    print(my_language.alphabet)
    print(my_language.generate_strings(3))


if __name__ == "__main__":
    main()
