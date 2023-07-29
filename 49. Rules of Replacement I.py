def rules_of_replacement_i(premises):
  """Prints the rules of replacement I for the premises."""
  
  # Check if the premises are in standard form.
  if not all(re.match(r"(A|E)I|O", premise) for premise in premises):
    return None
  
  # Apply the rules of replacement I.
  for premise in premises:
    if premise == "P or not P":
      print("Double Negation")
    elif premise == "P and P":
      print("Tautology")
    elif premise == "P or Q":
      print("Addition")
    elif premise == "P and not Q":
      print("Implication")
    elif premise == "not P and not Q":
      print("Exclusive Disjunction")
    elif premise == "P implies Q":
      print("Conjunction")
    else:
      print("Invalid")

def main():
  premises = ["P or not P", "P and P", "P or Q", "P and not Q", "not P and not Q", "P implies Q"]
  rules_of_replacement_i(premises)

if __name__ == "__main__":
  main()
