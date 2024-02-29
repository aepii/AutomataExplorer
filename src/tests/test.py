from classes.language import FormalLanguage
from classes.automata import State, Automata

def main():
    print("Formal Language Test: ")
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

    print("\nAutomata Test: ")
    my_state_a = State("q1", False)
    my_state_b = State("q2", True)

    my_state_a.add("a", my_state_b)
    my_state_a.add("b", my_state_a)
    my_state_b.add("b", my_state_a)

    my_automata = Automata([my_state_a, my_state_b], my_state_a)
    my_automata.process_input("bba")

if __name__ == "__main__":
    main()
