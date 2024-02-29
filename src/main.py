from classes.language import FormalLanguage


def main():
    my_language = FormalLanguage()
    my_language.add("c")
    my_language.add("b")
    my_language.add("a")

    print(my_language.alphabet)
    print(my_language.generate_strings(3))
    print(my_language.is_a_string(""))
    print(my_language.is_a_string("abc"))
    print(my_language.is_a_string("abfc"))
    print(my_language.is_a_string("A"))


if __name__ == "__main__":
    main()
