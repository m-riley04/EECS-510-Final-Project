from enum import Enum
    
# Initialize the constants for the class usage (DO NOT EDIT THESE INITIALIZATIONS)
PASTAS      = []
SAUCES      = []
ADDONS      = []
INGREDIENTS = []

class IngredientType(Enum):
    """Enum representing the type of ingredient"""
    PASTA = 0
    SAUCE = 1
    ADDON = 2
    
class Ingredient:
    """Class representing an ingredient"""
    def __init__(self, name: str, type: IngredientType):
        self.name = name
        self.type = type
    
    @staticmethod
    def isPasta(input) -> bool:
        return input in PASTAS
    
    @staticmethod
    def isSauce(input) -> bool:
        return input in SAUCES
    
    @staticmethod
    def isAddon(input) -> bool:
        return input in ADDONS
    
    @staticmethod
    def isIngredient(input) -> bool:
        return input in INGREDIENTS
    
    def __str__(self):
        return f"{self.name}"
    
    def __repr__(self):
        return f"{self.name}({self.type})"

def create_ingredient(name:str) -> Ingredient | None:
    """Creates an ingredient for a given name"""
    if name in PASTAS:
        return Ingredient(name, IngredientType.PASTA)
    elif name in SAUCES:
        return Ingredient(name, IngredientType.SAUCE)
    elif name in ADDONS:
        return Ingredient(name, IngredientType.ADDON)
    else:
        return None

### MAIN VARIABLES
# Input the actual values of the ingredient types
PASTAS: list[str]   = ["spaghetti"]
SAUCES: list[str]   = ["marinara", "alfredo", "butter", "carbonara"]
ADDONS: list[str]   = ["ground meat", "olive oil", "minced garlic", "chopped onion"]

# Generate the list of ingredients
INGREDIENTS: list[Ingredient] = [create_ingredient(ingredient) for ingredient in PASTAS + SAUCES + ADDONS]

# Create mappings between the ingredients and a specific letter
SYMBOLS: list[str] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAPPINGS: dict[str, Ingredient] = {}
for i, ingredient in enumerate(INGREDIENTS):
    MAPPINGS[SYMBOLS[i]] = ingredient