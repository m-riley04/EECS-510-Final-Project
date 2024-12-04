import os
from machine import Machine
from ingredients import INGREDIENTS, MAPPINGS

from PIL import Image
from automathon import NFA

def accept(A: Machine, w: str):
    # Run the input in the machine
    _ = A.run(w)
    
    # Return either "accept" or "reject"
    if _: return "accept"
    else: return "reject"
    
def parse_input_file(filename: str):
    # Initialize machine variables
    states: list[str] = []
    symbols: list[str] = []
    start_state: str = ""
    accept_states: list[str] = []
    transitions: dict[str, dict[str, set[str]]] = dict()
    
    # Read the input file
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Line 1: A whitespace-separated list of states
        states = lines[0].replace("\n", "").split(" ")
        
        # Line 2: A whitespace-separated list of symbols
        symbols = lines[1].replace("\n", "").split(" ")
        
        # Line 3: The start state
        start_state = lines[2].strip()
        
        # Line 4: A whitespace-separated list of accept states
        accept_states = lines[3].replace("\n", "").split(" ")
        
        # Line(s) 5+: Transitions
        transitions = {state: {} for state in states}
        for line in lines[4:]:
            from_state, symbol, to_state = line.strip().split()
            if symbol not in transitions[from_state]:
                transitions[from_state][symbol] = set()
            transitions[from_state][symbol].add(to_state)
        
        # Close the file
        file.close()
        
    # Print parsed values of NFA states
    print(f"States: {states}")
    print(f"Symbols: {symbols}")
    print(f"Start State: {start_state}")
    print(f"Accept States: {accept_states}")
    print("Transitions:")
    for state, transition in transitions.items():
        print(f"{state}: {transition}")
    
    # Visualize the NFA using graphiz
    nfa = NFA(
        q=set(states), 
        sigma=set(symbols), 
        delta=transitions, 
        initial_state=start_state, 
        f=set(accept_states))
    
    # Attempt to visualize using Graphviz
    try:
        # Initialize output names
        output_dir = "output"
        output_name = "nfa"
        output_path = output_dir + "/" + output_name
        
        # Check if output folder exists
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        
        # Create output image
        nfa.view(output_path)
        Image.open(output_path + ".gv.png").show()
    except Exception as e:
        print("ERROR: Unable to visualize NFA.")
        print(f"Details: {e}")
        
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
    parse_input_file("pasta_nfa.txt") 
    # test_machine() # Uncomment if you want original test machine behavior
    

if __name__ == "__main__":
    main()