from ingredients import Ingredient, IngredientType, MAPPINGS

class Machine:
    """Represents our machine (NFA)"""
    def __init__(self):
        pass
    
    def parse(self, input: str) -> list[Ingredient]:
        """Parses an input string into a list of ingredients in order"""
        _ = []
        for symbol in input:
            _.append(MAPPINGS[symbol])
        return _
    
    def run(self, input: str):
        # Parse the input
        ingredients: list[Ingredient] = self.parse(input)
        
        # Check if there is any input at all
        if len(ingredients) <= 0:
            print("Invalid input. Please enter at least one ingredient.")
            return
        
        # TRANSITION 1: Check if the first ingredient is a pasta
        if ingredients[0].type == IngredientType.PASTA:
            print(f"1. Begin by cooking the {ingredients[0]} pasta noodles.")
        else:
            print("Invalid input. Please enter a valid pasta.")
            return
        
        # TRANSITION(s) 2: Check for sauces and addons
        for i, ingredient in enumerate(ingredients[1:], 2):
            match (ingredient.type):
                case IngredientType.SAUCE:
                    print(f"{i}. Add {ingredient} sauce to the pasta.")
                    break
                case IngredientType.ADDON:
                    print(f"{i}. Add {ingredient} to the pasta.")
                    break
                case _:
                    print(f"Invalid input. Please enter a valid sauce or addon.")
                    return
        
        
        