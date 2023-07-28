def is_atomic(formula):
  """Returns True if formula is an atomic formula, False otherwise."""
  if not isinstance(formula, str):
    return False
  return formula in ["True", "False"]

def is_connective(formula):
  """Returns True if formula is a connective, False otherwise."""
  if not isinstance(formula, str):
    return False
  return formula in ["and", "or", "not"]

def is_variable(formula):
  """Returns True if formula is a variable, False otherwise."""
  if not isinstance(formula, str):
    return False
  return formula.isalpha()

def is_formula(formula):
  """Returns True if formula is a propositional logic formula, False otherwise."""
  if is_atomic(formula):
    return True
  elif is_connective(formula):
    if len(formula) == 1:
      return False
    elif is_formula(formula[0]) and is_formula(formula[1]):
      return True
    else:
      return False
  else:
    return False

def main():
  formulas = ["True", "False", "and", "or", "not", "P", "Q", "P and Q", "P or Q", "not P"]
  for formula in formulas:
    print(is_formula(formula))

if __name__ == "__main__":
  main()
