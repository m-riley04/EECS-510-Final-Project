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
        self.ingredients: dict[str, str] = {symbol: ingredients[i] for i, symbol in enumerate(self.symbols)}

    def print_formatted_steps(self, result: AcceptResult):
        if result:
            # The string is accepted, which means we have a valid "recipe"
            print("The dish is complete! Here are the steps:")
        else:
            # The string is not accepted, meaning the sequence is incomplete or invalid.
            print("The sequence of ingredients does not form a valid dish.")
            return

        # Print out the steps by parsing the path/transitions
        i: int = 1
        for transition in result.path:
            if len(transition) < 3:
                continue
            
            # Get the symbol from the transition
            symbol = transition.symbol
            
            # If symbol is not a lambda transition (~), print instruction
            if symbol != LAMBDA_SYMBOL and symbol in self.ingredients:
                # Get the ingredient map
                name = self.ingredients[symbol]

                # Print the step marker
                print(f"Step {i}: ", end="")

                # Check the type of ingredient and print the corresponding step
                if name in PASTA:
                    print(f"Boil and plate the {name} pasta noodles.")
                elif name in SAUCES:
                    print(f"Top the dish with {name} sauce.")
                elif name in ADDONS:
                    print(f"Prepare and add {name}.")
                else:
                    print(f"Add {name}.")

                # Increment step count
                i += 1

        return result
