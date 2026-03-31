# sequences.py
# Sequence Printer Test Project — v0.1.1
# Built by Claude (via Fetch and Carry pipeline, iter 1)

def print_sequence(name, items):
    print(name)
    print(", ".join(items))
    print()

def main():
    print_sequence("Numbers", ["1", "2", "3", "4", "5"])
    print_sequence("Alphabet", ["a", "b", "c", "d", "e", "f"])
    print_sequence("Colors", ["red", "yellow", "blue", "green", "orange", "purple"])
    print_sequence("Shapes", ["circle", "square", "triangle", "diamond"])
    print_sequence("One little Indians", [
        "one", "two", "three", "four", "five",
        "six", "seven", "eight", "nine", "ten"
    ])

if __name__ == "__main__":
    main()
