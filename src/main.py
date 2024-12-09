from automata.pasta_nfa import PastaNFA
import argparse

### GLOBAL CONSTANTS ###
DEBUG: bool                 = False
FORMATTED_STEPS: bool       = True
PRINT_PATH: bool            = True
NFA_FILENAME: str           = "machines/nfa.txt"

### PARSING CLI ARGUMENTS ###
parser = argparse.ArgumentParser(description="PastaNFA")
parser.add_argument("-m", "--machine_path", dest="machine_path", type=str, default=NFA_FILENAME, help="Path to the NFA/machine file to load.")
parser.add_argument("-i", "--input_string", dest="input_string", type=str, help="Input string to test on the machine.")
parser.add_argument("-d", "--debug", help="Enable debug output.", type=bool, default=DEBUG)
parser.add_argument("-p", "--print_path", dest="print_path", help="Print the path/trace of the input.", type=bool, default=PRINT_PATH)
parser.add_argument("-f", "--formatted_steps", dest="formatted_steps", help="Print the formatted steps of the input.", type=bool, default=FORMATTED_STEPS)
args = parser.parse_args()

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
    if bool(_) == True and args.print_path: 
        for t in _.path:
            print(t)

    # Print the formatted steps
    if args.formatted_steps: A.print_recipe(_)

def main():
    # Initialize NFA
    nfa: PastaNFA = PastaNFA(filename=args.machine_path, debug=args.debug)

    # Debug actions
    if args.debug:
        nfa.print()
        nfa.generate_diagram()
    
    # Get the input string if input is not specified
    w = args.input_string
    if w is None:
        w = format_input(input("Enter your ingredients: "))
    
    # Check if it accepts or returns the input
    accept(A=nfa, w=w)

if __name__ == "__main__":
    main()