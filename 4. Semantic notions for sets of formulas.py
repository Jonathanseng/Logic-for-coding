def is_tautology(formulas):
  """Returns True if formulas is a tautology, False otherwise."""
  for model in itertools.product([True, False], repeat=len(formulas)):
    if not all(truth_value(formula, model) for formula in formulas):
      return False
  return True

def is_contradiction(formulas):
  """Returns True if formulas is a contradiction, False otherwise."""
  for model in itertools.product([True, False], repeat=len(formulas)):
    if any(truth_value(formula, model) for formula in formulas):
      return False
  return True

def is_satisfiable(formulas):
  """Returns True if formulas is satisfiable, False otherwise."""
  for model in itertools.product([True, False], repeat=len(formulas)):
    if all(truth_value(formula, model) for formula in formulas):
      return True
  return False

def main():
  formulas = ["P", "not P"]
  print(is_tautology(formulas))
  print(is_contradiction(formulas))
  print(is_satisfiable(formulas))

if __name__ == "__main__":
  main()
