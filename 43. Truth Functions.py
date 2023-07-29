def truth_functions(variables):
  """Prints the truth table for a truth function."""
  
  # Initialize the truth table.
  truth_table = []
  for values in itertools.product([True, False], repeat=len(variables)):
    truth_table.append(values)
  
  # Print the truth table.
  for values in truth_table:
    print(values)

def main():
  variables = ["P", "Q"]
  truth_functions(variables)

if __name__ == "__main__":
  main()
