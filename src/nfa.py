import os
from dataclasses import dataclass
from PIL import Image
from automathon import NFA as VisualNFA
from state import State

LAMBDA_SYMBOL: str = "~"

@dataclass
class AcceptResult:
    """
    Class representing the return value for the "accept" method of an NFA
    """
    accepted: bool
    path: list[str]

    def __repr__(self):
        if self.accepted: return "accept"
        return "reject"
    
    def __str__(self):
        if self.accepted: return "accept"
        return "reject"
    
    def __bool__(self):
        return self.accepted
    
    def __len__(self):
        return len(self.path)

class NFA:
    """
    Class representing an NFA built from an input file.
    """
    def __init__(self, filename:str, debug:bool=False) -> None:
        # Initialize machine variables
        self.states: set[State] = {}
        self.symbols: set[str] = {}
        self.start_state: State = None
        self.accept_states: set[State] = {}
        self.transitions: dict[State, dict[str, set[State]]] = {}
        
        # Initialize other variables
        self.debug = debug
        
        # Parse the input file
        self.parse_input_file(filename)
        
    def find_state(self, name:str) -> State:
        """
        Finds a state by name.
        """
        for s in self.states:
            if s.name == name:
                return s
        return None
    
    def lambda_closure(self, states: set[State]) -> set[State]:
        """
        Computes the lambda closure of the given set of states (all states reachable from the input states via zero or more -transitions)
        """
        closure = set(states)
        stack = list(states)

        while stack:
            current_state = stack.pop()
            # Check if there are epsilon transitions from current_state
            if current_state.name in self.transitions and LAMBDA_SYMBOL in self.transitions[current_state.name]:
                for next_state in self.transitions[current_state.name][LAMBDA_SYMBOL]:
                    if next_state not in closure:
                        closure.add(next_state)
                        stack.append(next_state)

        return closure

    def accept(self, w: str) -> AcceptResult:
        """
        Checks if the given string is accepted by the NFA.
        Returns an AcceptResult object holding the acceptance results.
        """
        # Initialize return value
        result: AcceptResult = AcceptResult(False, [])
        
        # Start with epsilon-closure of the start state
        current_states = self.lambda_closure({self.start_state})
        
        # For each symbol in the input string
        for symbol in w:
            next_states = set()

            # For each state currently reachable, add transitions on 'symbol' if they exist
            for state in current_states:
                if state.name in self.transitions and symbol in self.transitions[state.name]:
                    # Record transition
                    result.path.append(f"{state} {symbol} {self.transitions[state.name][symbol]}")

                    # Update next states set
                    next_states.update(self.transitions[state.name][symbol])

            # After consuming 'symbol', take epsilon-closure of the set of reachable states
            current_states = self.lambda_closure(next_states)
        
        # Check if any current state is an accept state
        for s in current_states:
            if s in self.accept_states:
                result.accepted = True
                break

        # Return the result
        return result
    
    def get_states_as_strings(self) -> list[str]:
        """
        Gets the list of states as a list of strings.
        """
        return [s.name for s in self.states]
    
    def get_accepting_states_as_strings(self) -> list[str]:
        """
        Gets the list of accepting states as a list of strings.
        """
        return [s.name for s in self.accept_states]
    
    def parse_input_file(self, filename: str) -> bool:
        """
        Parses the input file
        """
        # Read the input file
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Line 1: A whitespace-separated list of states
            self.states = [State(s) for s in lines[0].replace("\n", "").split(" ")]
            
            # Line 2: A whitespace-separated list of symbols
            self.symbols = lines[1].replace("\n", "").split(" ")
            
            # Line 3: The start state
            _ = lines[2].strip()
            self.start_state = self.find_state(name=_)
            
            # Line 4: A whitespace-separated list of accept states
            _ = lines[3].replace("\n", "").split(" ")
            self.accept_states = [self.find_state(name=s) for s in _]
            
            # Line(s) 5+: Transitions
            self.transitions = {state.name: {} for state in self.states}
            for line in lines[4:]:
                from_state, symbol, to_state = line.strip().split()
                # Find states from names
                from_state = self.find_state(from_state)
                to_state = self.find_state(to_state)
                # Create transition
                if symbol not in self.transitions[from_state.name]:
                    self.transitions[from_state.name][symbol] = set()
                self.transitions[from_state.name][symbol].add(to_state)
            
            # Close the file
            file.close()
        
        # Debug print
        if self.debug: print(f"Parsed input file {filename} successfully!")
        
    def print(self):
        """
        Prints the main values of the NFA (states, symbols, start state, accept state(s), and transitions)
        """
        print(f"States: {self.states}")
        print(f"Symbols: {self.symbols}")
        print(f"Start State: {self.start_state}")
        print(f"Accept States: {self.accept_states}")
        print("Transitions:")
        for state, transition in self.transitions.items():
            print(f"{state}: {transition}")
            
    def show_diagram(self, output_dir:str="output", output_name:str="nfa"):
        """
        Displays a diagram of the NFA using Graphviz.
        Prints error message if it is not possible.
        """
        # Copy states as just strings
        _states_strs = self.get_states_as_strings()
        _accept_strs = self.get_accepting_states_as_strings()
        
        # Visualize the NFA using graphiz
        visual_nfa = VisualNFA(
            q=_states_strs, 
            sigma=self.symbols, 
            delta=self.transitions, 
            initial_state=self.start_state.name, 
            f=_accept_strs)
        
        # Attempt to visualize using Graphviz
        try:
            # Initialize output path
            output_path = output_dir + "/" + output_name
            
            # Check if output folder exists
            if not os.path.exists(output_dir):
                os.mkdirs(output_dir)
            
            # Create output image
            visual_nfa.view(output_path)
            Image.open(output_path + ".gv.png").show()
        except Exception as e:
            print("ERROR: Unable to visualize NFA.")
            print(f"Details: {e}")
        