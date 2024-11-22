from machine import Machine
from ingredients import INGREDIENTS, MAPPINGS

def accept(A: Machine, w: str):
    # Run the input in the machine
    _ = A.run(w)
    
    # Return either "accept" or "reject"
    if _: return "accept"
    else: return "reject"

def main():
    # Print out the possible ingredients and their corresponding symbol
    print("Ingredients:")
    for symbol, ingredient in MAPPINGS.items():
        print(f"- {symbol}: {ingredient}")
        
    # Get the input string
    inputString = input("Enter your ingredients: ")
    
    # Initialize the machine
    machine = Machine()
    
    # Test the machine against the input string
    print(accept(A=machine, w=inputString))

if __name__ == "__main__":
    main()