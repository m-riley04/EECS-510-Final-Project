class State:
    """
    Represents a state in a finite state machine
    """
    def __init__(self, name):
        self.name: str = name
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name