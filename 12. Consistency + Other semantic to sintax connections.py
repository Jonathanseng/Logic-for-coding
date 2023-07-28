def consistency(formulas):
  """Returns True if formulas is consistent, False otherwise."""
  for formula in formulas:
    if not is_satisfiable([formula]):
      return False
  return True

def semantic_to_syntactic(formula):
  """Returns the syntactic form of formula."""
  if formula == "True":
    return "True"
  elif formula == "False":
    return "False"
  elif formula == "not P":
    return "not " + formula[1:]
  elif formula == "P and Q":
    return formula[0:1] + " and " + formula[2:]
  elif formula == "P or Q":
    return formula[0:1] + " or " + formula[2:]
  else:
    raise ValueError(f"Invalid formula: {formula}")

def main():
  formulas = ["P", "not P", "P and Q", "P or Q"]
  print(consistency(formulas))
  for formula in formulas:
    print(semantic_to_syntactic(formula))

if __name__ == "__main__":
  main()
