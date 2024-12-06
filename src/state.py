class State:
    def __init__(self, name):
        self.name: str = name
        self.inbound: set[State] = {}
        self.outbound: set[State] = {}
        
    def add_transition(self, symbol, to_state):
        if symbol not in self.outbound:
            self.outbound[symbol] = set()
        self.outbound[symbol].add(to_state)
        if to_state not in self.inbound:
            self.inbound[to_state] = set()
        self.inbound[to_state].add(self)
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name