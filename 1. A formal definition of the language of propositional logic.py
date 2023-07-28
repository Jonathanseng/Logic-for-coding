def is_propositional_logic(formula):
  """Returns True if formula is a propositional logic formula, False otherwise."""
  if not isinstance(formula, str):
    return False
  for token in formula.split():
    if token not in ["True", "False", "and", "or", "not"]:
      return False
  return True

def main():
  formulas = ["True", "False", "and", "or", "not"]
  for formula in formulas:
    print(is_propositional_logic(formula))

if __name__ == "__main__":
  main()
