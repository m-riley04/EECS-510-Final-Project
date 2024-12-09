from dataclasses import dataclass
from automata.models.transition import Transition

@dataclass
class AcceptResult:
    """
    Class representing the return value for the "accept" method of an NFA
    """
    accepted: bool
    path: list[Transition]

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