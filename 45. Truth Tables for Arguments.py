def truth_table_argument(argument):
  """Prints the truth table for an argument."""
  
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
    print(" ".join(row))

def main():
  argument = ["P", "Q", "P implies Q", "Therefore, Q"]
  truth_table_argument(argument)

if __name__ == "__main__":
  main()
