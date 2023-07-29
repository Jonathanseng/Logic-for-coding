def rules_of_implication_ii(premises):
  """Prints the rules of implication II for the premises."""
  
  # Check if the premises are in standard form.
  if not all(re.match(r"(A|E)I|O", premise) for premise in premises):
    return None
  
  # Identify the major, minor, and conclusion terms.
  major_term = premises[0][0]
  minor_term = premises[1][0]
  conclusion_term = premises[2][0]
  
  # Apply the rules of implication II.
  if minor_term == conclusion_term:
    print("Contradiction")
  elif minor_term in premises[0]:
    print("Simplification")
  elif minor_term in premises[1]:
    print("Conjunction")
  else:
    print("Invalid")

def main():
  premises = ["P implies Q", "Not Q", "Therefore, not P"]
  rules_of_implication_ii(premises)

if __name__ == "__main__":
  main()
