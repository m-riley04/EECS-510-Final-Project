from automata.models.acceptresult import AcceptResult
from automata.nfa import NFA, LAMBDA_SYMBOL

### CONSTANTS ###
PASTA = ["spaghetti", "fettuccini", "macaroni"]
SAUCES = ["marinara", "alfredo", "pesto"]
ADDONS = ["ground beef", "chicken", "olive oil", "garlic", "onions", "broccoli"]
INGREDIENTS = PASTA + SAUCES + ADDONS

class PastaNFA(NFA):
    """
    A subclass of NFA that represents our pasta dish recipe machine.
    """
    def __init__(self, filename:str, debug:bool = False, ingredients: list[str] = INGREDIENTS):
        super().__init__(filename=filename, debug=debug)

        # Generate a dictionary of symbol-ingredient pairs
        self.ingredients = {symbol: ingredients[i] for i, symbol in enumerate(self.symbols)}

    def accept(self, w: str) -> AcceptResult:
        # Call parent accept method to get standard acceptance result
        result = super().accept(w)

        if result:
            # The string is accepted, which means we have a valid "recipe"
            print("The dish is complete! Here are the steps:")
        else:
            # The string is not accepted, meaning the sequence is incomplete or invalid.
            print("The sequence of ingredients does not form a valid dish.")

        # Print out the steps. The path gives us transitions in the form:
        # "q0 A q1", "q1 B q2", etc.
        # We can parse these lines to identify the symbols and translate them.
        for i, step in enumerate(result.path, 1):
            # Each step is something like: "q0 A q1"
            parts = step.split()  # ["q0", "A", "q1"]
            if len(parts) == 3:
                # The middle part is the symbol, e.g., "A"
                symbol = parts[1]
                
                # If the symbol is not a lambda (~) transition, print instruction
                if symbol != LAMBDA_SYMBOL and symbol in self.ingredients:
                    # Get the ingredient map
                    ingredient_name = self.ingredients[symbol]

                    # Print the step marker
                    print(f"Step {i}: ", end="")

                    # Check the type of ingredient and print the corresponding step
                    if symbol in PASTA:
                        print(f"Boil and add the {ingredient_name} pasta noodles.")
                    elif symbol in SAUCES:
                        print(f"Top the dish with {ingredient_name} sauce.")
                    elif symbol in ADDONS:
                        print(f"Prepare and add {ingredient_name}.")
                    else:
                        print(f"Add {ingredient_name}.")

        return result
