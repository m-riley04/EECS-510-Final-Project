from automata.pasta_nfa import PastaNFA

### GLOBAL CONSTANTS ###
DEBUG: bool                 = False
FORMATTED_STEPS: bool       = True
NFA_FILENAME: str           = "machines/nfa.txt"

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
    
    # Get the input string
    inputString = input("Enter your ingredients: ")
    
    # Check if it accepts or returns the input
    accept(A=nfa, w=inputString)

if __name__ == "__main__":
    main()