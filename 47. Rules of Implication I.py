def rules_of_implication_i(premises):
  """Prints the rules of implication I for the premises."""
  
  # Check if the premises are in standard form.
  if not all(re.match(r"(A|E)I|O", premise) for premise in premises):
    return None
  
  # Identify the major, minor, and conclusion terms.
  major_term = premises[0][0]
  minor_term = premises[1][0]
  conclusion_term = premises[2][0]
  
  # Apply the rules of implication I.
  if major_term == conclusion_term:
    print("Modus Ponens")
  elif major_term in premises[1]:
    print("Modus Tollens")
  else:
    print("Invalid")

def main():
  premises = ["P implies Q", "P", "Therefore, Q"]
  rules_of_implication_i(premises)

if __name__ == "__main__":
  main()
