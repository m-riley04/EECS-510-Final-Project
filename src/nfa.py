import os
from dataclasses import dataclass
from PIL import Image
from automathon import NFA as VisualNFA
from state import State

class NFA:
    def __init__(self, filename:str, debug:bool=False) -> None:
        # Initialize machine variables
        self.states: set[State] = []
        self.symbols: set[str] = []
        self.start_state: State = None
        self.accept_states: set[State] = []
        self.transitions: dict[State, dict[str, set[State]]] = dict()
        
        # Initialize other variables
        self.debug = debug
        
        # Parse the input file
        self.parse_input_file(filename)
        
    def find_state(self, name:str) -> State:
        """Finds a state by name"""
        for s in self.states:
            if s.name == name:
                return s
        return None
    
    def accept(self, string:str)-> bool:
        """Checks if the given string is accepted by the NFA"""
        current_states: set[State] = { self.start_state }
        for symbol in string:
            next_states: set = {}
            for state in current_states:
                if symbol in self.transitions[state.name]:
                    next_states.update(self.transitions[state.name][symbol])
            current_states = next_states
        return any(state in self.accept_states for state in current_states)
    
    def get_states_as_strings(self) -> list[str]:
        return [s.name for s in self.states]
    
    def get_accepting_states_as_strings(self) -> list[str]:
        return [s.name for s in self.accept_states]
    
    def parse_input_file(self, filename: str) -> bool:
        """Parses the input file"""
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
            self.accept_states = [self.states[i] for i in range(len(_)) if _[i] == self.states[i].name]
            
            # Line(s) 5+: Transitions
            self.transitions = {state.name: {} for state in self.states}
            for line in lines[4:]:
                from_state, symbol, to_state = line.strip().split()
                if symbol not in self.transitions[from_state]:
                    self.transitions[from_state][symbol] = set()
                self.transitions[from_state][symbol].add(to_state)
            
            # Close the file
            file.close()
        
        # Debug print
        if self.debug: print(f"Parsed input file {filename} successfully!")
        
    def print(self):
        """Prints the main values of the NFA (states, symbols, start state, accept state(s), and transitions)"""
        print(f"States: {self.states}")
        print(f"Symbols: {self.symbols}")
        print(f"Start State: {self.start_state}")
        print(f"Accept States: {self.accept_states}")
        print("Transitions:")
        for state, transition in self.transitions.items():
            print(f"{state}: {transition}")
            
    def show_diagram(self, output_dir="output", output_name="nfa"):
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
        