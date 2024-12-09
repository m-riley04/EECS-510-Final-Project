from automata.pasta_nfa import PastaNFA

### GLOBAL CONSTANTS ###
DEBUG: bool         = False
NFA_FILENAME: str   = "machines/nfa.txt"

def accept(A: PastaNFA, w: str) -> None:
    """
    Tests a given string on a given machine.
    Prints either "accept" with the path/trace, or "reject".
    """
    # Run the input in the machine
    _ = A.accept(w)
    
    # Print the acceptance result
    print(_)

    # Print the path if accepted
    if bool(_) == True: 
        for t in _.path:
            print(t)

def main():
    # Initialize NFA
    nfa: PastaNFA = PastaNFA(filename=NFA_FILENAME, debug=DEBUG)
    nfa.print() # Display parsed NFA info
    
    # Get the input string
    inputString = input("Enter your ingredients: ")
    
    # Check if it accepts or returns the input
    accept(A=nfa, w=inputString)

if __name__ == "__main__":
    main()