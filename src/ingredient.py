from enum import Enum

PASTAS = ["spaghetti"]
SAUCES = ["marinara", "alfredo", "butter", "carbonara"]
ADDONS = ["ground meat", "olive oil", "minced garlic", "chopped onion"]
INGREDIENTS = PASTAS + SAUCES + ADDONS

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
    
    def isPasta(self, input) -> bool:
        return input in PASTAS
    
    def isSauce(self, input) -> bool:
        return input in SAUCES
    
    def isAddon(self, input) -> bool:
        return input in ADDONS
    
    def isIngredient(self, input) -> bool:
        return input in INGREDIENTS