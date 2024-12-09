from automata.pasta_nfa import PastaNFA

### GLOBAL CONSTANTS ###
DEBUG: bool                 = True
FORMATTED_STEPS: bool       = True
NFA_FILENAME: str           = "machines/nfa.txt"

def format_input(s: str) -> str:
    """
    Cleans and formats input so it is most compatable with our machine.
    """
    # TODO: Add more cleaning/formatting here? (.upper(), removing characters, etc.)
    return s.strip()

def accept(A: PastaNFA, w: str) -> None:
    """
    Tests a given string on a given machine.
    Prints either "accept" with the path/trace, or "reject".
    """
    # Run the input in the machine
    _ = A.accept(w=w)
    
    # Print the acceptance result and path (if accepted)
    print(_)
    if bool(_) == True: 
        for t in _.path:
            print(t)

    # Print the formatted steps
    if FORMATTED_STEPS: A.print_formatted_steps(_)

def main():
    # Initialize NFA
    nfa: PastaNFA = PastaNFA(filename=NFA_FILENAME, debug=DEBUG)

    # Debug actions
    if DEBUG: 
        nfa.print()
        nfa.generate_diagram()
    
    # Get the input string
    w = format_input(input("Enter your ingredients: "))
    
    # Check if it accepts or returns the input
    accept(A=nfa, w=w)

if __name__ == "__main__":
    main()