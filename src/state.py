class State:
    def __init__(self, name):
        self.name: str = name
        
    def __str__(self):
        return self.name
    
    def __repr__(self):
        return self.name