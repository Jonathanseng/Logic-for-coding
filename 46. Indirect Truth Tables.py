def indirect_truth_table(argument):
  """Prints the truth table for an argument using indirect reasoning."""
  
  # Initialize the truth table.
  truth_table = []
  for values in itertools.product([True, False], repeat=len(argument)):
    truth_table.append(values)
  
  # Print the truth table.
  for values in truth_table:
    row = []
    for value in values:
      if value:
        row.append("T")
      else:
        row.append("F")
    
    # Check if the argument is valid using indirect reasoning.
    if values[-1] == "T" and not values[0]:
      print("Invalid")
    elif values[-1] == "F" and values[0]:
      print("Valid")
    else:
      print("Cannot determine validity")

def main():
  argument = ["P", "P implies Q", "Therefore, not Q"]
  indirect_truth_table(argument)

if __name__ == "__main__":
  main()
