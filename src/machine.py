from ingredient import Ingredient

class Machine:
    """Represents our machine (NFA)"""
    def __init__(self):
        pass
    
    def parse(self, input):
        # TODO: Implement parsing from string into array
        return input
    
    def run(self, input: str) -> str:
        # Parse the input
        parsed = self.parse(input)
        
        