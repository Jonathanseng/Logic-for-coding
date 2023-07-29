def rules_of_replacement_ii(premises):
  """Prints the rules of replacement II for the premises."""
  
  # Check if the premises are in standard form.
  if not all(re.match(r"(A|E)I|O", premise) for premise in premises):
    return None
  
  # Apply the rules of replacement II.
  for premise in premises:
    if premise == "not (P or Q)":
      print("De Morgan's I")
    elif premise == "not (P and Q)":
      print("De Morgan's II")
    elif premise == "(P or Q) or R":
      print("Commutation")
    elif premise == "(P and Q) and R":
      print("Associativity")
    elif premise == "P or (Q and R)":
      print("Distribution")
    else:
      print("Invalid")

def main():
  premises = ["not (P or Q)", "not (P and Q)", "(P or Q) or R", "(P and Q) and R", "P or (Q and R)"]
  rules_of_replacement_ii(premises)

if __name__ == "__main__":
  main()
