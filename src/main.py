from automata.models.acceptresult import AcceptResult
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

def accept(A: PastaNFA, w: str) -> AcceptResult:
    """
    Tests a given string on a given machine.
    Returns an AcceptResult containing either "accept" with the path/trace, or "reject".
    """
    return A.accept(w=w)
    
def print_output(A: PastaNFA, result: AcceptResult, print_path: bool, print_formatted: bool) -> None:
    """
    Prints the acceptance result and the path (if accepted).
    """
    print(result)
    if bool(result) == True and print_path: 
        for t in result.path:
            print(t)

    # Print the formatted steps
    if print_formatted: 
        print("\n== Recipe ==")
        A.print_recipe(result)

def main():
    # Initialize NFA
    nfa = PastaNFA(filename=args.machine_path, debug=args.debug)

    # Debug actions
    if args.debug:
        nfa.print()
        nfa.generate_diagram()
    
    # Get the input string if input is not specified
    w = args.input_string
    if w is None:
        w = format_input(input("Enter your ingredients: "))
    
    # Check if it accepts or returns the input
    result = accept(A=nfa, w=w)
    
    # Print the output
    print_output(A=nfa, result=result, print_path=args.print_path, print_formatted=args.formatted_steps)

if __name__ == "__main__":
    main()