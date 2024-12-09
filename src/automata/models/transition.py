from dataclasses import dataclass

from automata.models.state import State

@dataclass
class Transition:
    """
    Represents a transition from a state and symbol to a set of states
    """
    from_state: State
    symbol: str
    to_state: set[State]
    
    def __repr__(self):
        return f"{self.from_state} {self.symbol} {self.to_state}"
    
    def __str__(self):
        return f"{self.from_state} {self.symbol} {self.to_state}"
    
    def __len__(self):
        count: int = 0
        count += self.from_state is not None
        count += self.symbol is not None
        count += self.to_state is not None
        return count