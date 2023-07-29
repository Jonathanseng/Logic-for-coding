def truth_table(proposition):
  """Prints the truth table for a proposition."""
  
  # Initialize the truth table.
  truth_table = []
  for values in itertools.product([True, False], repeat=len(proposition)):
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
  proposition = ["P", "Q", "P and Q"]
  truth_table(proposition)

if __name__ == "__main__":
  main()
