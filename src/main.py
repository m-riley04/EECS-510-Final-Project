from machine import Machine
from ingredients import INGREDIENTS, MAPPINGS

def main():
    # Print out the possible ingredients and their corresponding symbol
    print("Ingredients:")
    for symbol, ingredient in MAPPINGS.items():
        print(f"- {symbol}: {ingredient}")
        
    # Get the input string
    inputString = input("Enter your ingredients: ")
    
    # Run the input string through the machine
    machine = Machine()
    machine.run(input=inputString)

if __name__ == "__main__":
    main()