from machine import Machine
from ingredients import INGREDIENTS, MAPPINGS
from nfa import NFA

### GLOBAL CONSTANTS ###
DEBUG:bool = False
NFA_FILENAME:str = "nfa.txt"

def accept(A: NFA, w: str) -> None:
    """
    Tests a given string on a given machine.
    Prints either "accept" with the path/trace, or "reject".
    """
    # Run the input in the machine
    _ = A.accept(w)
    
    # Print the acceptance result
    print(_)

    # Print the path if accepted
    if _ == True: 
        for t in _.path:
            print(t)

def main():
    # Initialize NFA
    nfa: NFA = NFA(filename=NFA_FILENAME, debug=DEBUG)
    nfa.print() # Display parsed NFA info
    
    # Get the input string
    inputString = input("Enter your ingredients: ")
    
    # Check if it accepts or returns the input
    accept(A=nfa, w=inputString)

if __name__ == "__main__":
    main()