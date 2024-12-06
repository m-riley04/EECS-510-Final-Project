from machine import Machine
from ingredients import INGREDIENTS, MAPPINGS
from nfa import NFA

### GLOBAL CONSTANTS ###
DEBUG:bool = False
NFA_FILENAME:str = "nfa.txt"

def accept(A: NFA, w: str):
    # Run the input in the machine
    _ = A.accept(w)
    
    # Return either "accept" or "reject"
    if _: return "accept"
    else: return "reject"
        
def test_machine():
    """Original testing implementation of the pasta NFA"""
    # Print out the possible ingredients and their corresponding symbol
    print("Ingredients:")
    for symbol, ingredient in MAPPINGS.items():
        print(f"- {symbol}: {ingredient}")
        
    # Get the input string
    inputString = input("Enter your ingredients: ")
    
    # Initialize the machine
    machine = Machine()
    
    # Test the machine against the input string
    print(accept(A=machine, w=inputString))

def main():
    # Initialize NFA
    nfa: NFA = NFA(filename=NFA_FILENAME, debug=DEBUG)
    
    # Get the input string
    inputString = input("Enter your ingredients: ")
    
    # Return if it accepts or rejects the input string
    accept(A=nfa, w=inputString)

if __name__ == "__main__":
    main()