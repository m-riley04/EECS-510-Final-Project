from machine import Machine
from ingredients import INGREDIENTS, MAPPINGS

from automathon import NFA
import automathon

def accept(A: Machine, w: str):
    # Run the input in the machine
    _ = A.run(w)
    
    # Return either "accept" or "reject"
    if _: return "accept"
    else: return "reject"
    
def parse_input_file(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()
        # Line 1: A whitespace-separated list of states
        states: list[str] = lines[0].replace("\n", "").split(" ")
        
        # Line 2: A whitespace-separated list of symbols
        symbols: list[str] = lines[1].replace("\n", "").split(" ")
        
        # Line 3: The start state
        start_state: str = lines[2].strip()
        
        # Line 4: A whitespace-separated list of accept states
        accept_states: list[str] = lines[3].replace("\n", "").split(" ")
        
        # Line(s) 5+: Transitions
        transitions = {state: {} for state in states}
        for line in lines[4:]:
            from_state, symbol, to_state = line.strip().split()
            if symbol not in transitions[from_state]:
                transitions[from_state][symbol] = set()
            transitions[from_state][symbol].add(to_state)
        
        # Print parsed transitions of NFA states 
        for state, transition in transitions.items():
            print(f"{state}: {transition}")
        
        # Visualize the NFA using graphiz
        nfa = NFA(
            q=set(states), 
            sigma=set(symbols), 
            delta=transitions, 
            initial_state=start_state, 
            f=set(accept_states))
        
        try:
            nfa.view("nfa")
        except Exception as e:
            print("Graphviz not found or another error occurred. Unable to visualize NFA.")
            print(f"Error: {e}")
        
        # Close the file
        file.close()

def main():
    parse_input_file("automaton.txt")
    
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

if __name__ == "__main__":
    main()