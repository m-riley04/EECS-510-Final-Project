from dataclasses import dataclass

class Transition:
    pass

@dataclass
class State:
    name: str
    into: list[Transition]
    out: list[Transition]

@dataclass
class Transition:
    symbol: str
    a: str
    b: str

class NFA:
    def __init__(self, filename) -> None:
        self.parse_file(filename)
    
    def parse_file(self, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            
            # Parse states
            self.states: list[str] = lines[0].replace("\n", "").split(" ")
            
            # Parse symbols
            self.symbols: list[str] = lines[1].replace("\n", "").split(" ")
            
            # Parse start state
            self.start_state: list[str] = lines[2].strip()
            
            # Parse accept states
            self.accept_states: list[str] = lines[3].replace("\n", "").split(" ")
            
            # Parse transitions
            self.transitions: list[Transition] = []
            for line in lines[4:]:
                # Create transition from line
                _ = line.replace("\n", "").split(" ")
                self.transitions.append(Transition(a=_[0], symbol=_[1], b=_[2]))